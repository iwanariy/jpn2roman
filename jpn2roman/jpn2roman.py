#!/bin/python2.7
# coding: utf-8
import requests
from xml.dom.minidom import parseString
import os
import dotenv
dotenv.load_dotenv(".env")

# Constant
URL = 'http://jlp.yahooapis.jp/FuriganaService/V1/furigana'


def _get_result_xml(search_keyword):
    # Get APPID
    appid = os.environ['APPID']

    # Create payload
    payload = {'appid': appid, 'sentence': search_keyword}

    responce = requests.post(URL, data=payload)

    # Show responce
    # print u"text: %s" % responce.text
    # print u"encoding: %s" % responce.encoding

    return responce


def _extract_data_from_xml(responce):
    # from xml.dom.minidom import parse, parseString
    doml = parseString(responce.content)

    # Get Word DOM
    results = doml.getElementsByTagName('Result')
    word_lists = results.item(0).getElementsByTagName('WordList')
    words = word_lists.item(0).getElementsByTagName('Word')

    # Return
    row = []

    for word in words:
        try:
            surface = word.getElementsByTagName('Surface').item(0).childNodes[0].data
            furigana = word.getElementsByTagName('Furigana').item(0).childNodes[0].data
            roman = word.getElementsByTagName('Roman').item(0).childNodes[0].data
        except:
            surface = word.getElementsByTagName('Surface').item(0).childNodes[0].data
            furigana = surface
            roman = surface

        row.append((surface, furigana, roman))

    return row


def get_roman_from_jpn(search_keyword):
    responce = _get_result_xml(search_keyword)

    row = _extract_data_from_xml(responce)

    return row
