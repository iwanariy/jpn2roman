#!/bin/python2.7
# coding: utf-8
import requests
import os
import dotenv
dotenv.load_dotenv(".env")

# Constant
URL = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana'


if __name__ == '__main__':
    search_word = u"山田太郎"

    # Get APPID
    appid = os.environ['APPID']

    # Create payload
    payload = {'appid': appid, 'sentence': search_word}

    r = requests.post(URL, data=payload)

    # Show responce
    print u"text: %s" % r.text
    print u"encoding: %s" % r.encoding
