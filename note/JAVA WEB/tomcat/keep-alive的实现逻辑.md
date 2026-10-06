https://blog.csdn.net/lies_joker/article/details/103758040

https://www.jianshu.com/p/9ed60827177c

https://hongjiang.info/how-tomcat-implements-keep-alive/

https://www.jianshu.com/p/09e2f32a74dd



https://segmentfault.com/a/1190000016637212

http://blog.sina.com.cn/s/blog_e59371cc0102ux5w.html





https://www.fatalerrors.org/a/long-connection-socket-and-tomcat-containers.html



# keepalive和HTTP Keep-Alive的区别

HTTP Keep-Alive是多个http请求复用同一个tcp连接。

keepalive是工作不正常时回收资源用的。在一定时间后发送探测报文，如果客户端挂了就关闭连接，相对于“keep”更像是“check”。



同时，tcp连接的关闭也是由服务端/客户端执行了socket.close()才会关闭tcp连接。OS不会去关闭正常工作的连接，所以keepalive对HTTP Keep-Alive没有影响。



一般讨论tcp长连接短连接时，指的是其应用层是否为长连接。

所以讨论http时，tcp的长连接实际上就是http的长连接。

长连接短连接只是是否复用tcp而不是时间上的概念。



keepalive默认关闭，HTTP Keep-Alive默认开启。



