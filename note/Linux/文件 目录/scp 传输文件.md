前提条件：



上传，服务器要开启写入权限；



本地和服务器都要安装有 scp 包；



 



如何传输：



1. 从服务器上下载文件；



scp username@servername:远程目录/文件名 本地目录

```shell
scp root@192.168.0.101:/var/www/test.txt /var/www/local_dir
```







(把 192.168.0.101 上的 /var/www/test.txt 文件下载到本地目录 /var/www/local_dir)



 



2. 从服务器上下载目录；



```javascript
scp -r username@servername:远程目录 本地目录
```

例：scp -r root@192.168.0.101:/var/www/test /var/www/



(把 192.168.0.101 上的 /var/www/test 目录下载到本地目录 /var/www)



 



3. 上传本地文件到目标服务器；



scp /本地目录/文件名 username@servername:远程目录

例：scp /var/www/test.txt root@192.168.0.101:/var/www/



(把本地目录 /var/www/ 下的 test.txt 文件上传到 192.168.0.101 的 /var/www/ 目录中)



 



4. 上传本地目录到目标服务器；



scp -r 本地目录 username@servername:远程目录

例：scp -r /var/www/local_dir root@192.168.0.101:/var/www/



(把本地目录 /var/www/local_dir 上传到服务器的 /var/www/ 目录)





# 免密码

`scp` 想“后台跑”，核心问题不是 `nohup`，而是它默认需要交互式输入密码；一旦放到后台，终端输入就没了，所以会卡住。

最常用的做法有这几种：

- 最推荐：改成免密登录，用 SSH key
- 临时方案：用 `sshpass` 非交互传密码
- 交互式后台：用 `screen` / `tmux`
- 已经连着机器时：先前台启动，认证完再挂起转后台

**推荐做法**

先配 SSH 免密，这样 `scp` 就能直接 `nohup`：

```bash
ssh-keygen -t ed25519
ssh-copy-id user@host
```

然后后台执行：

```bash
nohup scp /path/to/file user@host:/path/to/dest > scp.log 2>&1 &
```

如果目录递归复制：

```bash
nohup scp -r /path/to/dir user@host:/path/to/dest > scp.log 2>&1 &
```

**临时传密码**

如果暂时不能配密钥，可以用 `sshpass`：

```bash
nohup sshpass -p '你的密码' scp /path/to/file user@host:/path/to/dest > scp.log 2>&1 &
```

但这个方案有风险：

- 密码会出现在命令历史里
- 进程列表里可能被看到
- 不适合生产环境长期使用

稍好一点是从文件读密码：

```bash
nohup sshpass -f /path/to/passfile scp /path/to/file user@host:/path/to/dest > scp.log 2>&1 &
```

并且限制权限：

```bash
chmod 600 /path/to/passfile
```

**更稳的交互式后台**

如果你只是想“关终端也不断”，`tmux` 或 `screen` 比 `nohup` 更合适：

```bash
tmux new -s copyjob
scp /path/to/file user@host:/path/to/dest
```

然后按：

```bash
Ctrl-b d
```

即可脱离会话，任务继续跑。之后可重新进入：

```bash
tmux attach -t copyjob
```

**先认证再丢后台**

也可以这样：

```bash
scp /path/to/file user@host:/path/to/dest
```

输入密码后，在传输进行中按：

```bash
Ctrl-z
bg
disown
```

这样它会转到后台继续跑。但这个方法不如 `tmux` 稳，也依赖 shell 行为。

**补充**

- 想看是否还在跑：`ps -ef | rg scp`
- 想看日志：`tail -f scp.log`
- 大文件传输更推荐 `rsync`，可断点续传：

```bash
nohup rsync -avP /path/to/file user@host:/path/to/dest > rsync.log 2>&1 &
```

如果你愿意，我可以直接给你一套“免密 + 后台 + 日志”的完整命令，按你的本地路径和远端地址替你写好。