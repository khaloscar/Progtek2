""" bst.py

Student: Oscar Jansson
Mail: oscar.jansson.0363@student.uu.se
Reviewed by: Carl Fröding
Date reviewed: 2025-09-23
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): # given function
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    # def contains(self, k) # Ex8: write recursive contains
    def contains(self, k):
        # Recursion -> call some _contains()
        # A bt is a bt of bt
        # base case, empty tree, empty Node? 
        if self is None:
            return False
        else:
            def _contains(n: BST.Node):
                if n is None:
                    return False
                elif k == n.key:
                    return True
                elif k < n.key:
                    return _contains(n.left)
                elif k > n.key:
                    return _contains(n.right)
            return _contains(self.root)

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #        Ex9   
        # Have to check all nodes
        # A node either has a child or it doesnt +1 height or +0
        # All nodes w/ same depth can be added w/ boolean algebra
        # All depth added algebraicly -> level order
        # So like, depends on how to go through the tree, i.e tree traversals,
        # preorder, postorder, inorder and level order

        # Get a BTS
        if self.root is None:
            return 0
        else:
            # Get the biggest number from either the left or right child
            def _height(n: BST.Node):
                if n is None:
                    return False
                else:
                    left = _height(n.left)
                    right = _height(n.right)

                        # a * (a > b) is needed because python evaluates the first truth in an 'or' statement
                        # I.e T or 5 -> T
                        # but F or 5 -> 5
                        # and 3 or 5 -> 3
                        # but we want 3 or 5 -> 5 
                        # or just do 1 + max(left,right)
                    return 1 + (left*(left > right) or right*(left <= right))
            

            return _height(self.root)

    def __str__(self):                #     Ex10
        if self.root is None:
            return '<>'
        else:
            it = iter(self)
            strout = f'<{next(it)}'
            for e in it:
                strout += f', {e}'
            return strout + '>'


    def to_list(self):                      #   Ex11
        return [n for n in self]
    """
Complexity of to_list:
    1. we create the list as we go, n complexity
"""

    def to_LinkedList(self):    #     Ex12
        if self.root is None:
            return LinkedList() 
        else:
            output = LinkedList()

            # A generator from highest to lowest
            def _it_bw(n: BST.Node):
                if n.right:
                    yield from _it_bw(n.right)
                yield n.key
                if n.left:
                    yield from  _it_bw(n.left)
                    
            for e in _it_bw(self.root):
                output.first = output.Node(e, output.first)
            return output




        
    """
Complexity of _LinkedList:
    Create the list as we go, n complexity
"""
    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Ex13
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # enter r.right
                # go left as far as possible
                r.key = self._smol(r.right)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def _smol(self, r):
        # Find leftmost node
        # Effectively rmv it
        # and pass back its value to parent call
        # convoluted
        if r.left is None:
            return r.key, r.right
        else: 
            key, r.left = self._smol(r.left)
            return key


def main():
    t = BST()
    l = LinkedList()
    for x in [5, 3, 8, 1, 4, 6, 9, 2, 7]:
        t.insert(x)
        l.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    l2 = t.to_LinkedList()
    print(f'l1: {l}')
    print(f'l2: {l2}')

if __name__ == "__main__":
    main()


"""
Ex14: What is the generator good for?
==============================

1. computing size? -> n complexity
    Size of BST is just the amnt of nodes,
    so the generator is an okay choice, n complexity
2. computing height?
        no, creating the generator destroys the information contained in each node
        (and implicitly for the structure) 
        it flattens the tree to a ordered 1D vector
        e.g: 
            seq [1,2,3,4,5] to BST | depth 5
            seq [3,1,4,2,5] to BST | depth 3
            so if we flatten the tree, we have to "rebuild" it 
            to get the height back i.e redo whatever is already done
        maybe a generator could work better if you somehow yield each level
3. contains?
    contains is a search operation, which for the average tree is log n, and a h operation
    flattening the tree is a linear search which on average and worst case is n operation
4. insert?
    no, inserting something requires the Node object. Besides, searching for the correct place
    to insert a value is a log n operation for the average tree
5. remove?
    same spiel as above


"""
