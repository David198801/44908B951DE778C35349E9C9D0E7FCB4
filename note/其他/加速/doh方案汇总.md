本来想让ai撸一个代理cloudflare或者google doh的服务，但是发现论坛里已经有大量现成的doh可以使用，又省下了不少token 

1. 首先是始皇的2个doh

- `https://aaa.ddd.oaifree.com/query-dns`
- `https://i4cm5lqxfu.cloudflare-gateway.com/dns-query`
  [OAIFree 这个域名换了个方式跟大家见面](https://linux.do/t/topic/1150121)

1. 赛博菩萨提供的doh

- 上面始皇帖子里有配置方式，需要验证支付方式
- `https://[任意子域].cloudflare-gateway.com/dns-query` [Cloudflare的 DNS over https(DOH)地址](https://linux.do/t/topic/697242)

1. 佬友的公益doh

- https://linux.do/t/topic/1177430/110
- https://linux.do/t/topic/1373963

1. 公共doh

- [分享的海量DoH](https://linux.do/t/topic/1151240)

1. 自建doh，以下方案均免费

- Adguard
  - [Zeabur 免费部署 Adguard Home 私人DNS 教程 加密DNS 自建DOH](https://linux.do/t/topic/1214569)
  - [ClawCloud Run 免费部署 Adguard Home 私人DNS 教程 加密DNS 自建DOH](https://linux.do/t/topic/1221286)
- RethinkDNS
  - [GitHub - serverless-dns/serverless-dns: The RethinkDNS resolver that deploys to Cloudflare Workers, Deno Deploy, Fastly, and Fly.io](https://github.com/serverless-dns/serverless-dns)
- doh-cf-workers
  - [GitHub - tina-hello/doh-cf-workers: DNS-over-HTTPS proxy on Cloudflare Workers](https://github.com/tina-hello/doh-cf-workers)