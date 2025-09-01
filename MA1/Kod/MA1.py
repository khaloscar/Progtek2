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
    if n==0 or m==0:
        return 0
    else:
        if m < n:
            return m + multiply(m, n-1)
        else:
            return n + multiply(m-1,n)

def harmonic(n: int) -> float:              
    """Ex2: Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1.0
    else:
        return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """ Ex3: Returns the binary representation of x """
    if x < 0:
        return '-' + get_binary(-1*x)
    
    if x == 1:
        return '1'
    elif x == 0:
        return '0'
    else:
        return get_binary(x//2) + get_binary(x%2)


def reverse_string(s: str) -> str:        
    """Ex4: Returns the s reversed """
    
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


def largest(a: iter):                     
    """Ex5: Returns the largest element in a"""
    if len(a) == 1:
        return a[0]
    
    if len(a) >= 2:
        tmp = largest(a[1:])
        if a[0] > tmp:
            return a[0]
        else:
            return tmp



def count(x, s: list) -> int:                
    """Ex6: Counts the number of occurences of x on all levels in s"""
    if s == []:
        return 0
    else:
        sum = 0
        for e in s:
            if e == x:
                sum += 1
            elif type(e) == list:
                sum += count(x,e)
        return sum


def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """Ex7: Returns a string of instruction ow to move the tiles """
    if n == 0:
        return []
    else:
        return bricklek(f,h,t,n-1) + [f+'->'+t] + bricklek(h,t,f,n-1)


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
    
def fib_mem(n):
    memory = {0:0, 1:1}
    
    def fib_mem2(n):
        if n not in memory:
            memory[n] = fib_mem2(n-1) + fib_mem2(n-2)
        return memory[n]
    
    return fib_mem2(n)



def main():
    print('\nCode that demonstates my implementations\n')

    print(bricklek('f', 't', 'h', 2))

    print('\n\nCode for analysing fib and fib_mem\n')
    #########
    # a)
    #########
    print(f'\nfib part a)')

    n1 = 20
    n2 = 30
    t0 = time.perf_counter()
    fib(n1)
    t1 = time.perf_counter()
    print(f'    Runtime: {(t1-t0)} s')
    tfib1 = t1-t0

    t0 = time.perf_counter()
    fib(n2)
    t1 = time.perf_counter()
    print(f'    Runtime: {t1-t0} s')
    tfib2 = t1-t0

    print(f'    Runtime frac: {tfib2/tfib1}')
    print(f'    Theoretical frac: {1.618**(n2-n1)}')
    print(f'    C calculated: {(tfib2/tfib1)**(1/(n2-n1))}')

    #########
    # b)
    #########
    print(f'\nfib part b)')

    t0 = time.perf_counter()
    fib(30)
    t1 = time.perf_counter()
    tbase = t1-t0
    tfib50 = 1.618**(50-30)*tbase
    tfib100 = 1.618**(100-30)*tbase

    print(f'    Estimated runtime fib(50): {tfib50/60:.0f} min')
    print(f'    Estimated runtime fib(50): {tfib100/(3600*24*365):.0f} years')

    print(f'\nfib_mem(100)')
    t0 = time.perf_counter_ns()
    fib_mem(100)
    t1 = time.perf_counter_ns()
    print(f'    Time fib_mem(100): {t1-t0} ns')
    print(f'    100th fib number: {fib_mem(100)}')
  

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:

    t(n) = 2^n-1 complexity for the tile game, according to 
    lecture notes. Assuming each operation takes 1s, and n=50
    we get t(50) = 2^50-1 s. Which gives roughly 35702052 years

  Exercise 9: Time for Fibonacci:
    Verification of growth done in main under part a)

    Times for part b)
    Estimated runtime fib(50): 24 min
    Estimated runtime fib(50): 1307955 years

  Exercise 10: Time for fib_mem:
  
    Time fib_mem(100): 23300 ns
  
  
  
  Exercise 11: Comparison sorting methods:
    Insertion sort has O(n**2)
    Merge sort has O(n log n)

    Ins. sort:
        ins(10**3) = C * (10**3)**2 = 1s
        ins(10**6) = C * (10**6)**2 = (10**3)**2 * 1s
        ins(10**6) = C * (10**9)**2 = (10**6)**2 * 1s
    
    Merge sort:
        merge(10**3) = C * 10**3 log ( 10**3 ) = 1s
        merge(10**6) = 2 * 10**3 * 1s
        merge(10**9) = 3 * 10**6 * 1s

  Exercise 12: Comparison Theta(n) and Theta(n log n)

    tA(n) = n
    tB(n) = C * n * log n
    tB(10) = 1s => C = 1s / 10 * log 10 = 1/10
    tB(n) > tA(n)
    1/10 * n * log n > n
    log n > 10
    n > 10**10 (=bigbig)
  
  
"""
