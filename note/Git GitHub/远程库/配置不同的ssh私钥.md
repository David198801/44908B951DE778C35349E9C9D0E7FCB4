按平台地址指定密钥~/.ssh/config

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_github
```

指定项目ssh私钥

```shell
git config core.sshCommand "ssh -i ~/path/to/private_key"
```

