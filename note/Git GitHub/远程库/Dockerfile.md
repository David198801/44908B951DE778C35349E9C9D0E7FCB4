1. 创建一个目录，目录内创建Dockerfile文件

2. 执行 docker build -t alpine-git-ssh .

3. 执行 docker run -it --name git1 alpine-git-ssh /bin/bash

# alpine-git-ssh
```
FROM alpine:latest

RUN apk update && apk add --no-cache \
    bash \
    git \
    openssh-keygen \
    openssh-client

CMD ["/bin/bash"]
```

