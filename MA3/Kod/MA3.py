""" MA3.py

Student: Oscar Jansson
Mail:   oscar.jansson.0363@student.uu.se
Reviewed by: Carl Fröding
Date reviewed: 24-09-2025

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here

    x = [random.uniform(-1,1) for _ in range(n)]
    y = [random.uniform(-1,1) for _ in range(n)]

    # Create boolean mask for being on cirlce or not
    bool_circ = [x[e]**2 + y[e]**2 <= 1 for e in range(n)]

    x_square = []
    y_square = []
    x_circ = []
    y_circ = []
    for i, e in enumerate(bool_circ):
        if e:
            x_circ.append(x[i])
            y_circ.append(y[i])
        else:
            x_square.append(x[i])
            y_square.append(y[i])

    nc = len(y_circ)
    approx = 4*nc/n

    print(f'Number of points: {n}')
    print(f'Pi approximation: {approx}')

    name = f'PiApprox_{n}pts.png'
    print(f'Saving figure as "{name}"')

    plt.plot(x_circ,y_circ,'o',color='red')
    plt.plot(x_square,y_square,'o',color='blue')
    plt.grid()
    plt.savefig(f'{name}')

              

    return approx

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere
    # - Comprehension list
    # - lambda can be used together with say map
    # - map can be used to sort out the values within the sphere
    # - filter too??
    # - zip 

    # Need n pts in d dimensions -> list comprehension
    # Each sublist is a d dimensional point
    # we have n such points
    all_points = [[random.uniform(-1,1)**2 for _ in range(d)] for _ in range(n)] # do the squares immediately

    # Calculate square sum i.e x0^2 + ... + xd^2 for each point
    square_sum = list(map(sum,all_points))

    # Compare squared distance within sphere
    inside = list(filter(lambda x: x<=1, square_sum)) 

    # Get length of list to get amnt. of points within sphere
    nsph = len(inside)
 
    approx = nsph/n*2**d
    return approx

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere
    Vd = m.pi**(d/2)/m.gamma(d/2+1) 
    return Vd

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [n]*np, [d]*np)
        average = sum(results)/np

    return  average

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
  # np number or parallel proccesses

    # Generate data in parallel? Reuse main function, just get np chunks of data with some size
    sizes = [n//np]*(np-1) + [n//np + n%np]
    with future.ProcessPoolExecutor() as ex:
        result = mean(ex.map(sphere_volume, sizes, [d]*np))
    return result
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    print()
    n = 100000
    d = 2
    
    print(f"Approx volume of {d} dimentional sphere = {sphere_volume(n,d)} m^{d} ")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)} m^{d} ")

    n = 100000
    d = 11
    print(f"Approx volume of {d} dimentional sphere = {sphere_volume(n,d)} m^{d} ")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)} m^{d} ")

    #Ex3
    print()
    n = 100000
    d = 11
    values = []
    start = pc()
    for y in range (10):
        values.append(sphere_volume(n,d))
    average = mean(values)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start:.3}s")
    print(f'Average: {average:.3}')
    start = pc()
    avg = sphere_volume_parallel1(n,d)
    end = pc()
    print(f"Parallel1 time is: {end-start:.3}s ")
    print(f'Parallel1 avg is: {avg:.3}')

    #Ex4
    print()
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of d {d} and n {n}: {stop-start:.3}s")
    start = pc()
    res = sphere_volume_parallel2(n,d)
    stop = pc()
    print(f"Ex4: parallel time of d {d} and n {n}: {stop-start:.3}s")
    print(f'Parallel time result: {res}')

    
    

if __name__ == '__main__':
	main()
