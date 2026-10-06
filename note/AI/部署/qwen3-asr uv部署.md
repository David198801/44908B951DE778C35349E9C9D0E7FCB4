# 一步步安装
## 1. 部署
```javascript
# 1. 安装 uv（如尚未安装）
pip install uv

# 2. 创建 Python 3.12 虚拟环境到指定目录
uv venv --python 3.12 E:\a\qwen3-asr\py312

# 3. 激活虚拟环境
E:\a\qwen3-asr\py312\Scripts\activate

# 4. 安装 PyTorch (CUDA 12.8 版本)
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# 5. 安装其他依赖（包含 modelscope 用于下载模型）
uv pip install qwen-asr pydub silero-vad modelscope

# 6. 下载 Qwen3-ASR 模型到当前目录的 ./Qwen3-ASR-1.7B
modelscope download --model Qwen/Qwen3-ASR-1.7B --local_dir ./Qwen3-ASR-1.7B
```

## 2. 运行
```javascript
E:\a\qwen3-asr\py312\Scripts\activate

python batch_transcribe.py
```

# 先初始化项目来安装

```javascript
# 进入你的工作目录并初始化项目（自动指定 Python 3.12）
cd /d E:\a\qwen3-asr
uv init --python 3.12

# 安装 PyTorch (CUDA 12.8 版本)
# uv add 会自动创建 .venv 环境并写入 pyproject.toml
uv add torch torchvision torchaudio --index https://download.pytorch.org/whl/cu128

# 安装其他依赖
uv add qwen-asr pydub silero-vad modelscope

# 使用 uv run 执行模型下载（无需手动 activate 激活环境）
uv run modelscope download --model Qwen/Qwen3-ASR-1.7B --local_dir ./Qwen3-ASR-1.7B
```

