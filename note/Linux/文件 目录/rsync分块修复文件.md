# rsync从远程目录分块校验修复文件

```javascript
rsync -avP --checksum user@192.168.1.10:/data/bigfile.iso /mnt/d/download/bigfile.iso
```

## 参数解释

- `-a`
   归档模式，保留时间等属性
- `-v`
   显示详细信息
- `-P`
   等于 `--partial --progress`
  - `--progress`：显示进度
  - `--partial`：中断时保留已下载临时文件，便于续传
- `--checksum`
   不只看文件大小和时间，而是实际算校验来判断是否需要同步
   **这是修复损坏文件时很关键的选项**

------

# 如果你磁盘空间不足：用 `--inplace`

默认 rsync 常常会先生成一个临时文件，最后再替换原文件。
 这样更安全，但可能需要额外空间。

如果你的文件很大、磁盘空间紧张，可以用：

```bash
rsync -avP --checksum --inplace user@192.168.1.10:/data/bigfile.iso /mnt/d/download/bigfile.iso
```

## `--inplace` 的作用

直接在你现有的那个损坏文件上修改，只把差异块写进去。

## 风险

如果中途再次中断，本地文件会处于“正在被修补”的状态，不如默认模式安全。