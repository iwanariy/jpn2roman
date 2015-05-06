jpn2roman [![Build Status](https://travis-ci.org/narikin/jpn2roman.svg?branch=master)](https://travis-ci.org/narikin/jpn2roman)
---

Yahoo!デベロッパーネットワークさんの「ルビ振り」を使って、日本語をローマ字に変換してみた。  
（Webを叩く部分には、requestsを使用）


## Installation
```
pip install -r requirements.txt
```


## 準備
.envを作成し、AppIDを格納する。
```
APPID="Your application ID"
```


## Get started
```
python run.sh
```
山田太郎  
-> ('山田', 'やまだ', 'yamada')  
-> ('太郎', 'たろう', 'tarou')


## 制限
* APIの制限上、一日50,000件まで検索可能（2015/5/2現在）


## 注意点
* SubWordListがある場合も有りうるが、特に考慮せず。


## Special Thanks :)
* [Yahoo!Japanデベロッパーネットワーク > テキスト解析 > ルビ振り](http://developer.yahoo.co.jp/webapi/jlp/furigana/v1/furigana.html)
