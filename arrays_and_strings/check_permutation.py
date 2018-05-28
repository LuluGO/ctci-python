#!/usr/bin/python

import unittest

def check_permutation(string1, string2):
    """
    Given two strings returns True if one is permutation from the other, False otherwise.
    """
    if len(string1) != len(string2):
        return False

    char_list1 = [0 for c in range(128)]
    char_list2 = [0 for c in range(128)]

    for c1 in string1:
        char_list1[ord(c1)]+=1

    for c2 in string2:
        if char_list1[ord(c2)] == 0 or char_list2[ord(c2)] > char_list1[ord(c2)]:
            return False
        else:
            char_list2[ord(c2)]+=1
    return True

class TestCase(unittest.TestCase):
    """
    Test the result with multiple strings.
    """
    strings_true = ['ctci-python','itotc-icyhp']
    strings_false = ['hola', 'ho l']

    def perm_true(self):
        self.assertTrue(check_permutation(strings_true[0], strings_true[1]))

    def perm_false(self):
        self.assertFalse(check_permutation(strings_false[0], strings_false[1]))


if __name__ == '__main__':
    unittest.main()

