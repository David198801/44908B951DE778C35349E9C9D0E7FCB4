#!/usr/bin/env python3
from pathlib import Path
import logging
import os
import subprocess
import time

# 可按需增减
EXCLUDE_DIRS = {".svn", "__pycache__", ".git", "sofa-container", "target", "server"}
TARGET_BYTES = b'\x45\x2D\x53\x61\x66\x65\x4E\x65\x74'

def load_last_timestamp(state_file: Path) -> float:
    """
    读取 last_time.txt 中的时间戳。
    如果文件不存在、为空或格式非法，则默认使用当前时间往前 1 小时。
    """
    default_ts = time.time() - 3600

    if not state_file.exists():
        return default_ts

    content = state_file.read_text(encoding="utf-8").strip()
    if not content:
        return default_ts

    try:
        return float(content)
    except ValueError:
        logging.warning("last_time.txt 格式非法，已改用默认时间")
        return default_ts


def save_last_timestamp(state_file: Path, ts: float) -> None:
    """
    原子写入时间戳，避免写到一半程序中断导致文件损坏。
    """
    tmp_file = state_file.with_suffix(state_file.suffix + ".tmp")
    tmp_file.write_text(f"{ts:.6f}\n", encoding="utf-8")
    tmp_file.replace(state_file)


def checkYST(file_path: Path) -> bool:
    """
    检查文件二进制内容中是否包含指定字节片段。
    """
    try:
        with file_path.open("rb") as f:
            content = f.read()
        return TARGET_BYTES in content
    except Exception as exc:
        logging.warning("读取文件失败，跳过 %s：%s", file_path, exc)
        return False


def run_dec(file_path: Path) -> None:
    """
    调用已加入 PATH 的 dec 命令处理文件。
    """
    subprocess.run([r"E:\其他\old\d\java\java.exe", str(file_path)], check=True)


def iter_target_files(root: Path):
    """
    递归遍历 root 下的文件，并排除指定目录。
    """
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        base = Path(dirpath)
        for name in filenames:
            yield base / name


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    script_dir = Path(__file__).resolve().parent
    script_path = Path(__file__).resolve()
    state_file = script_dir / "last_time.txt"

    # 读取上次处理时间；本次扫描用“开始时间”作为水位线，避免漏掉运行期间新增的修改。
    last_timestamp = load_last_timestamp(state_file)
    scan_started_at = time.time()

    processed_count = 0

    for file_path in iter_target_files(script_dir):
        if file_path == state_file or file_path == script_path:
            continue

        try:
            mtime = file_path.stat().st_mtime
        except OSError as exc:
            logging.warning("跳过 %s，无法读取文件信息：%s", file_path, exc)
            continue

        if mtime <= last_timestamp:
            continue

        try:
            if not checkYST(file_path):
                continue
        except Exception as exc:
            logging.exception("checkYST 失败：%s，原因：%s", file_path, exc)
            continue

        try:
            run_dec(file_path)
            processed_count += 1
            logging.info("已处理：%s", file_path)
        except subprocess.CalledProcessError as exc:
            logging.error("dec 处理失败：%s，原因：%s", file_path, exc)

    try:
        save_last_timestamp(state_file, scan_started_at)
    except OSError as exc:
        logging.error("更新 last_time.txt 失败：%s", exc)
    else:
        logging.info("已更新处理时间戳：%.6f", scan_started_at)

    logging.info("完成，共处理 %d 个文件", processed_count)


if __name__ == "__main__":
    try:
        main()
    finally:
        input("运行完成，按回车退出...")
