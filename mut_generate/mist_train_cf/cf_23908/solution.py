"""
QUESTION:
Create a function named `std_deviation` that calculates the standard deviation of a given list of numbers. The input list is a collection of integers, and the function should return the standard deviation of the input data. Note: The standard deviation should be calculated using the population standard deviation formula.
"""

from math import sqrt

def std_deviation(data): 
    n = len(data) 
	 
    mean = sum(data) / n 
    sum_sqr = sum(pow(x - mean, 2) for x in data) 
    stdev = sqrt(sum_sqr / n) 
	
    return stdev