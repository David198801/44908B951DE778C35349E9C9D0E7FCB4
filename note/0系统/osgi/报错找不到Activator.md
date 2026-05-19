osgi java.lang.ClassNotFoundException: Activator



mf文件里导入jar包的路径没有加上“.”

```javascript
Bundle-ClassPath: .,
 lib/commons-codec-1.6.jar,
 lib/fastjson-1.2.83.jar,
 lib/itextpdf-sofa-5.5.13.jar,
 lib/jsch-0.1.51.jar,
 lib/SQLinForm-1.0.jar,
 lib/thumbnailator-0.4.8.jar
```

