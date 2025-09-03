# https://docs.python.org/3/library/unittest.html
"""
Unittests for the binary search tree methods

"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_height(self):
        bst = BST()
        self.assertEqual(bst.height(), 0)
        bst.insert(5)
        self.assertEqual(bst.height(), 1)
        bst.insert(2)
        self.assertEqual(bst.height(), 2)
        bst.insert(1)
        self.assertEqual(bst.height(), 3)
        bst.insert(7)
        self.assertEqual(bst.height(), 3)
        bst.insert(8)
        self.assertEqual(bst.height(), 3)
        bst.insert(9)
        self.assertEqual(bst.height(), 4)


if __name__ == "__main__":
    unittest.main()
