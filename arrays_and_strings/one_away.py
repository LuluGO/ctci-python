#!/usr/bin/python

import unittest

def one_away(string1, string2):
    """
    Given two strings returns True if only one edit is performed (insert, replace, remove), False otherwise.
    """
    string1 = list(string1.lower())
    string2 = list(string2.lower())

    if len(string1) == (len(string2)+1) or len(string1) == (len(string2)-1):
        diflen = True
        if len(string1) > len(string2):
            index = len(string2)
        else:
            index = len(string1)

    elif len(string1) == len(string2):
        diflen = False
        index = len(string1)

    else:
        return False

    edited = False
    for i in range(index):
        if string1[i] != string2[i] and diflen:
            if len(string1) > len(string2):
                string1.pop(i)
            else:
                string2.pop(i)
            if string1[i:] != string2[i:]:
                return False
            else:
               return True
        elif string1[i] != string2[i]:
            if not edited:
                edited = True
            else:            
                return False
    return True

class Test(unittest.TestCase):
    """
    Test with book strings.
    """
    data_true = [['pale', 'ple'], ['pale', 'pales'], ['pale', 'bale']]
    data_false = ['pale', 'bake']

    def test_true(self):
        for pairs in self.data_true:
            self.assertTrue(one_away(pairs[0],pairs[1]))

    def test_false(self):
        self.assertFalse(one_away(self.data_false[0],self.data_false[1]))

if __name__ == '__main__':
    unittest.main()


