#!/usr/bin/python
import unittest

def is_unique2(string):
    """
    Returns True if the string has all unique characters, False otherwise. Using hashtable.
    """
    if len(string) > 128:
        return False
   
    char_array = [False for k in range(128)]
    for char in string:
        key = ord(char)
        if char_array[key]:
            return False
        else: char_array[key] = True
    return True

class TestCase(unittest.TestCase):
    """
    Check the result with different strings.
    """
    unique_strings = ['python','ho la','']
    not_unique_strings = ['abal','4ghi pi',')i;()']

    def test_isunique(self):
        for test_s in self.unique_strings:
            self.assertTrue(is_unique2(test_s))

    def test_isnotunique(self):
        for test_s in self.not_unique_strings:
            self.assertFalse(is_unique2(test_s))

if __name__ == '__main__':
    unittest.main()

