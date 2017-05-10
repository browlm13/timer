#python 3

"""
	Timer - function performance evaulation
"""
import time

# time function duration and return time in milliseconds
def time_function( function, *args ):

	#time function
	start = time.time()
	function(*args)
	end = time.time()

	#time in milliseconds
	ex_duration = (end-start) * 1000.0
	return ex_duration

# time function n times return average in milliseconds
def average_runtime( n, function, *args ):

	#function trials
	runtimes = []
	for i in range(n): 
		runtimes.append( time_function(function,*args) )

	#average duration in milliseconds
	avg = sum(runtimes)/n
	return avg
