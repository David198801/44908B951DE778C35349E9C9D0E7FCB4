《Mineru 部署与使用指南》

# Mineru 部署与使用指南

*该教程基于Windows 11 系统 + RTX 4060Ti 显卡 + CUDA 12.9 + Anaconda + Python 3.11 环境*

## 📌 环境与硬件要求

- **操作系统**：建议Windows 11
- **显卡**：NVIDIA GeForce RTX 4060Ti 8GB（需要至少8g显存显卡）
- **CUDA 版本**：12.9（11.8及以上）
- **内存**：32GB（16g以上）
- **Python 环境**：Anaconda（推荐）
- **显卡驱动**：已正确安装并支持 CUDA （正常都是已经安装了的）

## 📦 第一步：安装 Anaconda

1. 访问官网下载安装包：https://www.anaconda.com/download
2. 下载对应的 **Windows 版本** 安装程序。
3. 一路点击 “下一步”，也可以选择自定义安装路径。
4. 安装完成后，打开「Anaconda Powershell Prompt（命令行）」。（一定要是这个，权限比较高。）

## 🧱 第二步：创建并激活虚拟环境

```Bash
conda create -n mineru python=3.11
conda activate mineru
```

说明：

- `mineru` 为虚拟环境名称，可自定义。
- `python=3.11` 指定使用的 Python 版本。

## 🚀 第三步：验证显卡与 CUDA 环境

1. 在 Anaconda 命令行中输入：

```Bash
nvidia-smi
nvcc --version
```

确认 CUDA 驱动是否正常工作，并查看版本号。

## 📥 第四步：安装 mineru 及依赖

1. 升级 pip：

```Bash
python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
```

1. 安装 `uv` 工具：

```Bash
pip install uv -i https://mirrors.aliyun.com/pypi/simple
```

1. 安装 mineru：

```Bash
uv pip install -U "mineru[core]" -i https://mirrors.aliyun.com/pypi/simple
```

## 🧪 第五步：安装 PyTorch（支持 CUDA 11.8/12.6/12.8等）

1. 访问 PyTorch 官网选择命令：https://pytorch.org/get-started/locally/
2. 如果你使用 CUDA 12.8，可执行如下命令（建议上官网查询，命令可能会有变化）：

```Bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

> 若 显卡不支持 CUDA 12.8 ，推荐使用 CUDA 12.6或者11.8 的版本。
>
> 安装过程可能会因网络问题下载失败或者缓慢，建议使用科学上网下载。

### ✅ 验证 PyTorch 安装

```Bash
python
>>> import torch
>>> print(torch.cuda.is_available())  # 返回 True 表示可用
>>> print(torch.cuda.get_device_name(0))  # 输出 4060Ti
>>> exit()
```
如果验证失败就直接在conda环境里卸载，重新安装
```Bash
pip uninstall -y torch torchvision torchaudio
```
## 📦 第六步：下载 mineru 模型

```Bash
$env:MINERU_MODEL_SOURCE = "modelscope" 
mineru-models-download
```

按提示选择：

- 模型源：`modelscope`
- 模型类型：`all`
- 若是遇到：$env:MINERU_MODEL_SOURCE = "modelscope" 报错，那就是没使用更高权限的命令行。

> ⚠️ 注意：若开启了科学上网，请务必关闭后再运行此步骤。

## 🧪 第七步：启动 Mineru 服务

### 方式一：API 模式

```Bash
mineru-api --host 0.0.0.0 --port 8000
```

访问地址：

```Plain
http://127.0.0.1:8000/docs
```

### 方式二：WebUI 模式

```Bash
mineru-gradio --server-name 0.0.0.0 --server-port 7860
```

访问地址：

```Plain
http://127.0.0.1:7860
```

## 🔁 第八步：重启后使用方式

1. 打开「Anaconda Prompt」
2. 激活虚拟环境：

```Bash
conda activate mineru
$env:MINERU_MODEL_SOURCE = "modelscope" 
```

1. 启动对应服务：
   1. `mineru-api` 或 `mineru-gradio` 即可
   2. 若是遇到：$env:MINERU_MODEL_SOURCE = "modelscope" 报错，那就是没使用更高权限的命令行。

注意：若是没有重启再去重新运行有概率遇到500报错码。

# 报错码处理

 400报错码   

 文件格式不对，不支持docs，pptx等格式？也许支持但需要调整参数。

 500报错码

  1.开始没有设置环境变量$env:MINERU_MODEL_SOURCE = "modelscope" 

  2.pytorch版本下载错误，按照验证pytorch安装模块去验证

  3.pytorch内部冲突（之前可以运行，突然就报500错误码的情况。），解决方法，重启电脑。

 其他报错码

 1.问ai

 2.去mineru官方文档里面找解决方案，里面有个专门的AI助手

## 🛠️ 常见问题处理

| 问题                                 | 处理方式                                   |
| ------------------------------------ | ------------------------------------------ |
| 安装卡住或太慢                       | 尝试使用阿里源、或开启科学上网             |
| torch.cuda.is_available() 返回 False | 检查 CUDA 驱动、PyTorch 版本与显卡是否兼容 |
| 下载模型失败                         | 确保未开启科学上网，或更换镜像源           |
| 中止运行                             | 可使用快捷键 Ctrl + C 强制终止             |