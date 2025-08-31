"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """ Ex1: Computes m*n using additions"""
    pass


def harmonic(n: int) -> float:              
    """Ex2: Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    pass


def get_binary(x: int) -> str:              
    """ Ex3: Returns the binary representation of x """
    pass


def reverse_string(s: str) -> str:        
    """Ex4: Returns the s reversed """
    pass


def largest(a: iter):                     
    """Ex5: Returns the largest element in a"""
    pass


def count(x, s: list) -> int:                
    """Ex6: Counts the number of occurences of x on all levels in s"""
    pass


def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """Ex7: Returns a string of instruction ow to move the tiles """
    pass


def fib(n: int) -> int:                      
    """ For Ex9: Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  
  
  
  Exercise 9: Time for Fibonacci:


  
  
  Exercise 10: Time for fib_mem:
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  
  
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  
  
"""
