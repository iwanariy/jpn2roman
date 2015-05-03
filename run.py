#!/bin/python2.7
# coding: utf-8
import requests
from xml.dom.minidom import parseString
import os
import dotenv
dotenv.load_dotenv(".env")

# Constant
URL = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana'


def get_result_xml():
    # Get APPID
    appid = os.environ['APPID']

    # Create payload
    payload = {'appid': appid, 'sentence': search_word}

    return requests.post(URL, data=payload)


if __name__ == '__main__':
    search_word = u"山田太郎"

    r = get_result_xml()

    # Show responce
    # print u"text: %s" % r.text
    # print u"encoding: %s" % r.encoding

    # from xml.dom.minidom import parse, parseString
    doml = parseString(r.content)

    # Get Word DOM
    results = doml.getElementsByTagName('Result')
    word_lists = results.item(0).getElementsByTagName('WordList')
    words = word_lists.item(0).getElementsByTagName('Word')

    for word in words:
        print word.getElementsByTagName('Surface').item(0).childNodes[0].data
        print word.getElementsByTagName('Furigana').item(0).childNodes[0].data
        print word.getElementsByTagName('Roman').item(0).childNodes[0].data
