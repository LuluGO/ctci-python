#!/usr/bin/python

import unittest

def pp(string):
    """
    Returns True if the string given is the permutation of a palindrome.
    """
    string = string.lower()
    char_count = [0 for k in range(128)]
    for char in string:
        char_count[ord(char)] +=1

    odd = 0
    if char_count[32] % 2:
        odd +=1
        char_count.pop(32)

    for count in char_count:
        if count % 2 != 0:
            odd +=1
        if odd > 2:
            return False
    else:
        return True

class Test(unittest.TestCase):
    """
    Test with test string from the book and not palindrome string case.
    """
    test_str = ['Tact Coa', 'pablito Clavo un clavito', 'tactcoapapa']

    def test_True(self):
        actual = pp(self.test_str[0])
        self.assertTrue(actual)

    def test_True2(self):
        actual = pp(self.test_str[2])
        self.assertTrue(actual)

    def test_False(self):
        actual = pp(self.test_str[1])
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()



