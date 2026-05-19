在CentOS上搭建NFS（网络文件系统）共享磁盘，可以让你通过网络与其他计算机共享文件和目录。以下是搭建NFS共享磁盘的步骤：

### 步骤 1: 安装NFS服务器

首先，你需要确保你的CentOS系统上安装了NFS服务。你可以使用以下命令来安装NFS服务：

```
sudo yum install nfs-utils
```

### 步骤 2: 创建共享目录

选择一个目录作为共享目录。例如，你可以创建一个名为`/nfs_share`的目录：

```
sudo mkdir -p /nfs_share
```

### 步骤 3: 配置NFS导出

编辑NFS的配置文件`/etc/exports`，添加你想要共享的目录和允许访问的客户端。例如，要共享`/nfs_share`目录给所有客户端，可以添加如下行：

全部映射匿名用户为root，生产需要创建单独用户并使用uid -g 用户名获取用户gid，-u获取uid

```
/root/nfs_share *(rw,sync,no_subtree_check,all_squash,anonuid=0,anongid=0)
```

这里，`*`表示所有客户端都可以访问，`rw`表示读写权限，`sync`表示数据同步写入磁盘，`no_root_squash`允许root用户具有完全访问权限，`no_subtree_check`可以提高性能。

### 步骤 4: 启动NFS服务

启动NFS服务并设置其开机自启：

```
sudo systemctl start nfs-server
sudo systemctl enable nfs-server
```

### 步骤 5: 导出并重新加载配置

导出新的共享目录并重新加载NFS服务配置：

```
sudo exportfs -arv
```

### 步骤 6: 配置防火墙（如果使用）

如果你的服务器使用了防火墙（如firewalld），需要允许NFS相关的端口。例如，允许NFS的2049端口：

```
sudo firewall-cmd --permanent --add-port=2049/tcp
sudo firewall-cmd --reload
```

### 步骤 7: 在客户端挂载NFS共享

在客户端机器上，你可以使用以下命令来挂载NFS共享：

-o noac为无缓存

```
sudo mount -t nfs -o noac <服务器IP>:/nfs_share /mnt/nfs_share
```

这里，`<服务器IP>`是你的CentOS服务器的IP地址，`/mnt/nfs_share`是客户端本地的挂载点。如果挂载点不存在，你需要先创建它：

```
sudo mkdir -p /mnt/nfs_share
```

### 步骤 8: 测试访问权限

在客户端尝试访问挂载的目录，确保一切工作正常：

```
ls /mnt/nfs_share
```

以上就是在CentOS上设置NFS共享磁盘的步骤。确保在设置过程中检查网络连接和防火墙设置，以确保无障碍的网络访问。如果你遇到任何问题，检查NFS日志文件（如`/var/log/messages`或使用`showmount -e <服务器IP>`来查看导出的文件系统）可能会提供有用的信息





# 取消挂载

| 场景                   | 命令                                                        | 说明                                 |
| :--------------------- | :---------------------------------------------------------- | :----------------------------------- |
| **基本取消挂载**       | `sudo umount /mnt/nfs_share`                                | 标准的取消挂载方式。                 |
| **设备繁忙时延迟卸载** | `sudo umount -l /mnt/nfs_share`                             | 立即断开，等访问停止后完成卸载。     |
| **设备繁忙时强制卸载** | `sudo umount -f /mnt/nfs_share`                             | 强制卸载（可能导致数据丢失，慎用）。 |
| **查看占用进程**       | `sudo lsof /mnt/nfs_share`或 `sudo fuser -m /mnt/nfs_share` | 找出导致"设备繁忙"的进程8。          |