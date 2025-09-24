'''
Module 3: A4, A5, B2
Exam on 2024-10-29
'''

class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def append(self, x):
        """A4: inserts a new node with the specified content as the last node in the list"""

class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.count = 1  # For use in task B2

        def __str__(self):
            return f'({self.key}, {self.count})'

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self
            if self.right:
                yield from self.right

    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.insert(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x.key) for x in self]) + '>'

    def __repr__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        """ Standard binary search tree insertion, not a part of B2
        """
        def insert(key, r):
            if r is None:
                return BST.Node(key)
            elif key < r.key:
                r.left = insert(key, r.left)
            elif key > r.key:
                r.right = insert(key, r.right)
            else:
                pass # Already there. Do nothing.
            return r

        self.root = insert(key, self.root)

    def sum_level(self, level):
        """ A5: Returns the sum of the key values of the node on level """

    #def _insert(self, key):
     #   """help function for B2"""
     #   pass

    #def insert(self, key):
    #    """B2: An insert method that maintain the count field in the nodes"""

if __name__ == "__main__":
    ###A4
    lst = LinkedList()
    print(lst)
    for i in [5,2,10,5]:
        l=lst.append(i)
        print(lst, l)
        
    ###A5
    inserts = (5, 8, 1, 3, 7, 2, 6, 9)
    print(f'Inserted keys: {inserts}')
    tree = BST(inserts)
    print('Level   Sum of keys')
    for level in (0, 1, 2, 3, 4):
        result = tree.sum_level(level)
        print(f'{level:3d} {result:10d}')

    ###B2
    inserts = (10, 5, 1, 7, 20, 30, 15, 17, 12)
    print(f'Inserted keys: {inserts}')
    tree = BST()
    for x in inserts:
        tree.insert(x)
        print(f'After inserting {x}: {repr(tree)}')