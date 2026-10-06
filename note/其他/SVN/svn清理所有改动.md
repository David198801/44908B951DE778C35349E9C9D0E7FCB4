# svn清理所有改动
```shell
svn revert -R .
svn cleanup --remove-unversioned --remove-ignored
svn update
```

