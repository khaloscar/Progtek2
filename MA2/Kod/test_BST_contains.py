# https://docs.python.org/3/library/unittest.html
"""
Unittests for the binary search tree methods

"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_contains(self):
        bst = BST()
        lst = [16, 3, 20, 4, 14, 9, 15, 25, 11, 18]
        self.assertEqual(bst.contains(1), False)
        self.assertEqual(bst.contains(None), False)


        for x in lst:
            bst.insert(x)
        
        self.assertEqual(bst.contains(16), True)
        self.assertEqual(bst.contains(3), True)
        self.assertEqual(bst.contains(20), True)
        self.assertEqual(bst.contains(18), True)
        self.assertEqual(bst.contains(7), False)
        self.assertEqual(bst.contains(30), False)



if __name__ == "__main__":
    unittest.main()
