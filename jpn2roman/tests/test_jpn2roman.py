# coding: utf-8

import unittest
from jpn2roman.jpn2roman import get_roman_from_jpn


class TestJpn2roman(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        # Get result
        results = get_roman_from_jpn(u"山田太郎")

        # Expected
        expected_0 = (u"山田", u"やまだ", u"yamada")
        expected_1 = (u"太郎", u"たろう", u"tarou")

        # Assertion
        self.assertEqual(expected_0, results[0])
        self.assertEqual(expected_1, results[1])

    def test_include_space(self):
        # Get result
        results = get_roman_from_jpn(u"山田　太郎")

        # Expected
        expected_0 = (u"山田", u"やまだ", u"yamada")
        expected_1 = (u"　", u"　", u"　")
        expected_2 = (u"太郎", u"たろう", u"tarou")

        # Assertion
        self.assertEqual(expected_0, results[0])
        self.assertEqual(expected_1, results[1])
        self.assertEqual(expected_2, results[2])


if __name__ == "__main__":
    unittest.main()
