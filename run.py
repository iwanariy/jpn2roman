#!/bin/python2.7
# coding: utf-8
from jpn2roman.converter import get_roman_from_jpn


def print_row(search_keyword, rows):
    print search_keyword
    for row in rows:
        print "\t%s\t%s\t%s" % row

if __name__ == '__main__':
    search_keyword = u"山田太郎"

    row = get_roman_from_jpn(search_keyword)

    print_row(search_keyword, row)
