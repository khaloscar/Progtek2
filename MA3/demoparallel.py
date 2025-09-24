# 1) Parallel programming is not very efficient in Python, for more info read about GIL https://realpython.com/python-gil/
# 2) The speedup depends on your hardware (assuming all executions are independent)
# 3) 'multiprocessing' (nothing returned) 'concurrent.futures' (something returned)

import concurrent.futures as future
from random import randint
from time import perf_counter as pc

def roll_dice(s,t):
	'''
	s: number of sides on the dice
	t: number of throws
	returns a list of length t, with the results
	'''
	return [randint(1,s) for _ in range(t)]


if __name__ == '__main__':

	n_side=6
	n_throws=20

	# serial execution (not parallelized)
	# print(roll_dice(n_side,n_throws))


	# n_processes=4
	# sides=n_processes*[n_side]
	# throws=[n_throws//n_processes for _ in range(n_processes)]

	# print(sides)
	# print(throws)

	# with future.ProcessPoolExecutor() as ex:
	# 	results = ex.map(roll_dice, sides, throws)
	# results=list(results)

	# print(results)
	# print([r for sublist in results for r in sublist])




	# n_throws=2400000

	# start = pc()
	# result=roll_dice(n_side,n_throws)
	# end = pc()
	# print(f"Serial process took {round(end-start, 2)} seconds")

	# for n_processes in [2,4,8]:
	# 	sides=n_processes*[n_side]
	# 	throws=[n_throws//n_processes for _ in range(n_processes)]

	# 	start = pc()
	# 	with future.ProcessPoolExecutor() as ex:
	# 		results = ex.map(roll_dice, sides, throws)
	# 	results=list(results)
	# 	result=[r for sublist in results for r in sublist]
	# 	end = pc()
	# 	print(f"Process {n_processes} threads took {round(end-start, 2)} seconds")

	