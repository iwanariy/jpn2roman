#!/bin/python2.7
# coding: utf-8
from lib.converter import get_roman_from_jpn


if __name__ == '__main__':
    search_keyword = u"山田太郎"

    row = get_roman_from_jpn(search_keyword)

    print row
