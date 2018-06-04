#!/usr/bin/python

import unittest

def urlfy(string, truelen):
    """
    Given a string returns the strings with the spaces replaced with %20.
    """
    reallen = len(string)
    string = list(string)

    for i in range(truelen - 1, -1, -1):
        print string
        if string[i] == ' ':
            string[reallen - 1] = '0'
            string[reallen - 2] = '2'
            string[reallen - 3] = '%'
            reallen = reallen - 3
        else:
            string[reallen - 1] = string[i]
            reallen = reallen - 1
    return ''.join(string)

class TestCase(unittest.TestCase):
    """
    Test function with book example.
    """

    def test_equal(self):
        self.assertEqual(urlfy('Mr John Smith    ', 13), 'Mr%20John%20Smith')

if __name__ == '__main__':
    unittest.main()

