```
yt-dlp --proxy "http://127.0.0.1:7890" --cookies cookies.txt --remote-components ejs:github
```

参数，使用导出的cookie和GitHub提供的js解析脚本






```javascript
yt-dlp https://youtube.com/xxxx
```

默认只下载了低画质mp4

**先安装ffmpeg**



列出视频格式

```javascript
-F
```

指定视频格式，列出的视频号+音频号，例如

```javascript
-f234+329
```

或

```javascript
-f "best[ext=mp4]"
```

下载播放列表
```javascript
yt-dlp --download-archive videos.txt  https://www.youtube.com/playlist?list=PL22iamDQYGnNBnvKFjmqE3Oj5OqqBYOVY -o '%(playlist_title)s[%(playlist_id)s]/%(title)s[%(id)s].%(ext)s'
```
