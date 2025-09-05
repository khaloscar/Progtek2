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
    
    def __lt__(self, b):
        return self.pnr < b.pnr

    def __le__(self,b):
        return self.pnr <= b.pnr

    def __eq__(self, b):
        return self.pnr == b.pnr
    
    def __gt__(self, b):
        return self.pnr > b.pnr

    def __ge__(self,b):
        return self.pnr >= b.pnr

    def __ne__(self, b):
        return self.pnr != b.pnr
    
       


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
        
        elif x == self.first.data:
            self.first = self.first.succ
            return True
        
        else:        
            f = self.first
            while f.succ:
                if x == f.succ.data:
                    f.succ = f.succ.succ
                    return True
                f = f.succ 
            return False


    def to_list(self):            # Ex4

        def _to_list(f):

            if f is None:
                return []
            else:
                return [f.data] + _to_list(f.succ)

        return _to_list(self.first)



    def __str__(self):            # Ex5

        if self.first is None:
            return '()'
        else:
            iterator = iter(self)
            output = f'({next(iterator)}'
            for e in iterator:
                output += f', {e}'

        return output + ')'

    def copy(self):
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        main for loop goes through all elements -> n
        inner while loop is basically the main for loop in reverse -> n
        so complexity is O(n^2).
    '''

    def copy(self):               # Ex6, Should be more efficient
        output = LinkedList()

        if self.first is None:
            return output
        
        else:
            def _copy(f):
                if f is None:
                    return None
                else:
                    return output.Node(f.data,
                                       _copy(f.succ))

            output.first = output.Node(self.first.data,
                                        _copy(self.first.succ))
            return output                  
    ''' Complexity for this implementation:
        ''A lst is a Node linked to a list of Nodes''
        Uses recursion w/ base case node None type
        Uses the fact that a lst object is a ordered chain
            from low to high integers
        I.e create new nodes in .copy as you iterate through self
        Pretty much n complexity
    '''


def main():
    plist = LinkedList()
    print(plist)
    p = Person('Anakin', 66)
    plist.insert(p)
    print(plist)
    q = Person('Mario', 64)
    plist.insert(q)
    print(plist)


    # Test code:


if __name__ == '__main__':
    main()
