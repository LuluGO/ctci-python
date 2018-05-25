#!/usr/bin/python
import unittest

def is_unique1(string):
    """
    Returns True if the string has all unique characters, False otherwise. Using python in operator.
    """
    string = list(string)

    if len(string) > 128:
        return False

    count = 0
    for i in string:
        count+=1
        if i in string[count:]:
            return False
    return True


class TestCase(unittest.TestCase):
    """
    Check the result with different strings.
    """
    unique_strings = ['python','ho la','']
    not_unique_strings = ['abal','4ghi pi',')i;()']

    def test_isunique(self):
        for test_s in self.unique_strings:
            self.assertTrue(is_unique1(test_s))

    def test_isnotunique(self):
        for test_s in self.not_unique_strings:
            self.assertFalse(is_unique1(test_s))

if __name__ == '__main__':
    unittest.main()

