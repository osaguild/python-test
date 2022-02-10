# memo

### Remoのipアドレスを調べる
 - Remoと同じnetworkに接続する。
 - コマンド叩く。`dns-sd -B _remo._tcp`
```commandline
Browsing for _remo._tcp
DATE: ---Wed 09 Feb 2022---
18:54:35.001  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
18:54:35.405  Add        2   6 local.               _remo._tcp.          Remo-XXXXXX
```
 - Instance Nameを指定してコマンド叩く。`dns-sd -G v4 Remo-XXXXXX.local`
```commandline
DATE: ---Wed 09 Feb 2022---
18:54:56.258  ...STARTING...
Timestamp     A/R    Flags if Hostname                               Address                                      TTL
18:54:56.262  Add 40000002  6 Remo-XXXXXX.local.                     192.168.11.3                                 120
```

### Remoから赤外線通信を送る
 - Remoのlocal-apiを叩く。データ部は各家電の赤外線信号に合わせる。
```commandline
curl -X POST http://192.168.11.3/messages -H "X-Requested-With: local" -d \
'{"format":"xx","freq":xx,"data":[xxx,xxx,...,xxx]}'
```

### 赤外線通信を解析する
 - リモコンをRemoに近づけ、解析したい赤外線信号のボタンを押す。
 - Remoのlocal-apiを叩いてデータを取得する。`curl http://192.168.11.3/messages -H "X-Requested-With: local"`
 - 取得したデータをeditorで見ながらパターン解析する。

### Tips:formatされたjsonを1行で出力する。
`cat remo_1.json | jq -c`
### Tips:remo.plでコードを指定して赤外線信号を生成する。
`perl remo.pl aa 5a 8f 12 4a 82`