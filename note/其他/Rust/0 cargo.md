### 新建项目

```shell
cargo new project1
```

### 构建

```shell
# cd进入项目目录
cargo build
# 构建release版本
cargo build --release
```

### 运行(会自动构建)
```shell
# cd进入项目目录
cargo run
```







# RUSTUP临时换源

更换 rustup 的更新源为国内镜像
如果你没有代理，或者不想为命令行配置代理，可以把 rustup 的更新服务器换成国内的镜像服务器，例如中国科学技术大学（USTC）的镜像。这样访问速度会快很多，也更稳定。

同样，在命令行中设置环境变量：

对于 PowerShell:

<POWERSHELL>
$env:RUSTUP_DIST_SERVER="https://rsproxy.cn"
$env:RUSTUP_UPDATE_ROOT="https://rsproxy.cn/rustup"

## 设置完之后，再尝试运行
rustup update
cargo clean
对于 CMD:

<CMD>
set RUSTUP_DIST_SERVER=https://rsproxy.cn
set RUSTUP_UPDATE_ROOT=https://rsproxy.cn/rustup

## 设置完之后，再尝试运行
rustup update
cargo clean
提示：为了让这个设置永久生效，你可以把这两个环境变量添加到系统的“高级系统设置” -> “环境变量”中。









---

# cargo换源

更换 Cargo 的镜像源为中国科学技术大学（USTC）镜像，可以显著加快 Rust 依赖包的下载速度。

以下是具体操作步骤：

### 1. 找到配置文件
Cargo 的配置文件位于用户目录下的 `.cargo` 文件夹中：
*   **Windows**: `C:\Users\你的用户名\.cargo\config` (如果没有 `config` 文件，就新建一个，或者叫 `config.toml`)
*   **Linux / macOS**: `~/.cargo/config`

### 2. 修改配置内容
使用编辑器打开 `config` 文件，将以下内容复制并覆盖进去。

**推荐使用“稀疏索引（Sparse Index）”方式**（Cargo 1.68 版本及以上支持，速度最快）：

```toml
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
```

**如果你的 Cargo 版本较低（低于 1.68）**，请使用传统的 Git 索引方式：

```toml
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

### 3. 注意事项
1.  **文件名扩展名**：在较新版本的 Cargo 中，推荐使用 `config.toml` 作为文件名，但 `config`（无后缀）依然有效。
2.  **生效确认**：配置完成后，下次运行 `cargo build` 或 `cargo check` 时，你应该能看到下载地址已经变为 `mirrors.ustc.edu.cn`。
3.  **其他镜像源**：如果 USTC 偶尔不稳定，你也可以换成字节跳动（rsproxy）或阿里源，格式是一样的。

### 4. 验证是否成功
在终端运行：
```bash
cargo fetch
```
如果看到类似 `Updating 'https://mirrors.ustc.edu.cn/...'` 的输出，说明配置已生效。

---

**附：字节跳动 (rsproxy) 镜像（目前国内速度最快且稳定之一）**
如果你发现 USTC 速度不理想，可以尝试这个：
```toml
[source.crates-io]
replace-with = 'rsproxy'

[source.rsproxy]
registry = "sparse+https://rsproxy.cn/index/"
```
