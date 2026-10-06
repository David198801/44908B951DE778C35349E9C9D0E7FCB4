# litellm转换opencode的genimi为openai格式
1. 创建并激活虚拟环境

```
uv venv --python 3.12 E:\p\litellm\py312
E:\p\litellm\py312\Scripts\activate
```

2. 安装litellm，同时指定fastapi版本
```
uv tool install "litellm[proxy]" --with "fastapi==0.140.6"
```

3. 写配置文件config.yaml
```yaml
general_settings: 
  master_key: "sk-1234"
model_list:
  - model_name: gemini-3.7-flash
    litellm_params:
      model: gemini/gemini-3.7-flash
      api_base: "https://opencode.ai/zen/v1"  # https://opencode.ai/zen/v1/models/gemini-3.7-flash
      api_key: "sk-XVSvMnQlY"
```
4. 启动litellm
```
litellm --config config.yaml
```

