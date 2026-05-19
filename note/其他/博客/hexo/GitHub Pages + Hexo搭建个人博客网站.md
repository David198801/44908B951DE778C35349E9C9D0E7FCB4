# GitHub Pages + Hexo搭建个人博客网站

[GitHub Pages + Hexo搭建个人博客网站，史上最全教程](https://blog.csdn.net/yaorongke/article/details/119089190)

1. 准备：GitHub、git、nodejs

2. 创建仓库

3. 安装Hexo

   ```javascript
   npm install -g hexo-cli
   hexo init hexo-blog
   cd hexo-blog
   ```

4. 基础操作

   ```javascript
   生成
   hexo g
   提交
   hexo deploy
   生成并提交
   hexo g -d
   启动本地
   hexo s
   创建文章
   hexo new post 测试文章
   ```

   

# 部署到一个仓库的不同分支

创建仓库后，在博客目录初始化本地仓库并推送到远程库的blog分支

```javascript
git init
git checkout -b blog

git remote add origin git@github.com:username/proj
git add .
git commit -m "init hexo source"
git push -u origin blog
```
安装部署插件：

```
npm install hexo-deployer-git --save
```

然后修改 Hexo 根目录下的 `_config.yml`：

```
deploy:
  type: git
  repo: git@github.com:username/proj
  branch: main
```

同时url也要设置成对应的路径

```
# URL
## Set your site url here. For example, if you use GitHub Page, set url as 'https://username.github.io/project'
url: https://username.github.io/blog
```

然后这样执行：

```
hexo clean
hexo generate
hexo deploy
```

Hexo 会把 `public/` 的内容推送到远程仓库的 `main` 分支



