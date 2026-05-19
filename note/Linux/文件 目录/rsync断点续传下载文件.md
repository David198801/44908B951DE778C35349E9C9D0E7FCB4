```shell
rsync -avP --append-verify user@server:/path/to/file /mnt/d/downloads/
```

结合免输密码

```javascript
sshpass -p "oracle#S5_konG" rsync -avP --append-verify -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" oracle@10.1.95.155:/u01/app/oracle/admin/ACS/dpdump/backup.dmp /f/dmp/backup.dmp
```

