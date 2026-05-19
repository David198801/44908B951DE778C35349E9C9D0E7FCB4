# docker部署

https://github.com/wulabing/xray_docker/tree/master/reality

```shell
EXTERNAL_PORT=443 && docker run -d --name xray_reality --restart=always --log-opt max-size=100m --log-opt max-file=3 -p $EXTERNAL_PORT:443 -e EXTERNAL_PORT=$EXTERNAL_PORT wulabing/xray_docker_reality:latest && sleep 3 && docker exec -it xray_reality cat /config_info.txt
```

订阅转换优先选自建 https://sublink.09430943.xyz/



# 订阅转换 ，ACL4SSR

https://suburl.v1.mk/

选clashR，全局global有效