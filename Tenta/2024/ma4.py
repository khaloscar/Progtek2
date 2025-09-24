'''
Module 4: A6, A7, B3, B4
Exam on 2024-10-29
'''

import random
import concurrent.futures as future
from functools import reduce

"""A6: write a one-line list comprehension to return all even elements in a list"""
def A6(lst):
    pass #return one line

def A7(n):
    """A7: use at least three concepts from Module 4 of the course"""
def A7_tester(n):
    """should give you the same answer as A7"""
    return n*(n+1)*(2*n+1)/6
"""For B3: matrix multiplication"""
def random_matrices(m,n,k):
    A = []
    for _ in range(m):
         res = [random.randrange(0, 10, 1) for _ in range(n)]
         A = A+[res]
    B = []
    for _ in range(n):
        res = [random.randrange(0, 10, 1) for _ in range(k)]
        B = B + [res]
    return A,B

def multiplication(A,B):
    """B3: matrix multiplication"""

"""B4: poker"""
def B4(n, n_processes):
    pass
if __name__ == "__main__":
    ###A6
    #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 99]
    #print(f"Even numbers: {A6(numbers)}")
    ###A7
    #print(A7(10))
    #print(A7_tester(10))
    """I apply the following concepts in A7(n): """
    ###B3
    #A, B= random_matrices(4,3,2)
    #print(A)
    #print(B)
    #C = multiplication(A,B)
    #print(C)
    ###B4
    #B4(10000, 4)
