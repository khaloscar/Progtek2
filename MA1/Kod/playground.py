import random as rnd
import time
import numpy as np

import sys
sys.setrecursionlimit(100000)

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
        
def largest2(a):
    b = a.copy()
    if len(b) == 1:
      return b[0]
    elif b[0]<b[1]:
        return largest(b[1:])
    else:
      b.pop(1)
      return largest(b)

me = []
wohlin = []

iterations = 10
for i in range(iterations):
    size = 1000
    ns = [i*2 for i in range(1, size)]
    times = []
    # Get complexity
    for i in ns:
        a = [rnd.randint(0, size) for _ in range(i)]

        print(f'Running size: {i}')
        t0 = time.time()
        largest(a)
        t1 = time.time()
        print(f"Time taken for size {i}: {t1-t0}")
        times.append(t1-t0)

    times2 = []
    # Get complexity
    for i in ns:
        a = [rnd.randint(0, size) for _ in range(i)]

        print(f'Running size: {i}')
        t0 = time.time()
        largest(a)
        t1 = time.time()
        print(f"Time taken for size {i}: {t1-t0}")
        times2.append(t1-t0)

    me.append(times)
    wohlin.append(times2)

me = np.mean(me, axis=0)
wohlin = np.mean(wohlin, axis=0)

# Log plot
import matplotlib.pyplot as plt

plt.semilogy(ns, me, "o-", label="Min")
plt.semilogy(ns, wohlin, "o-", label="Wohlin")
plt.xlabel("Input size (n)")
plt.ylabel("Time (s, log scale)")
plt.title("Semi-log plot of largest()")
plt.legend()
plt.show()