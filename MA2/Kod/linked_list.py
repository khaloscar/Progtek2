""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""
class Person: #for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          #   Ex1
        n = 0
        f = self.first
        while f:
            n +=1
            f = f.succ

        return n

    def mean(self):               
        pass

    def remove_last(self):       # Ex2
        f = self.first

        # Check if empty
        # Check if only one
        # Else loop, can maybe combine the others
        f = self.first
        if f == None:
            raise ValueError
        elif f.succ is None:
            last = f.data
            self.first = None
            return last
        else:
            while f:
                if f.succ.succ is None:
                    last = f.succ.data
                    f.succ = None
                    return last
                f = f.succ


    def remove(self, x):         # Ex3
        if self.first is None:
            return False
        
        if x == self.first.data:
            self.first = self.first.succ
            return True
        
        f = self.first
        while f.succ:
            if x == f.succ.data:
                f.succ = f.succ.succ
                return True
            f = f.succ 
        return False


    def to_list(self):            # Ex4
        pass
    

    def __str__(self):            # Ex5
        pass

    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 

    '''

    def copy(self):               # Ex6, Should be more efficient
        pass                      
    ''' Complexity for this implementation:

    '''


def main():
    lst = LinkedList()
    for x in [3, 1, 2, 6]:
        lst.insert(x)
    lst.print()
    lst.remove_last()
    lst.print()
    lst.remove_last()
    lst.print()
    lst.remove_last()
    lst.print()
    lst.remove_last()
    lst.print()

    print(lst.length())

    # Test code:


if __name__ == '__main__':
    main()
