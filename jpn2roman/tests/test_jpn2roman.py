# coding: utf-8

import unittest
from jpn2roman.jpn2roman import get_roman_from_jpn


class TestJpn2roman(unittest.TestCase):

    def setUp(self):
        print 'setUp'

    def test_hello_world(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
