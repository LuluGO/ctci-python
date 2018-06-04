#!/usr/bin/python

import unittest

def urlfy(string):
    """
    Replace all spaces with %20 in the string.
    """
    words = string.split()
    return words.join('%20')

class TestCase(unittest.TestCase):
    """
    Test result with book example.
    """
    test_string = ['Mr John Smith    ','Mr%20John%20Smith']

    def check_equal(self):
        self.assertEqual(urlfy(test_string[0]), test_string[1])

if __name__ == '__main__':
    unittest.main()
