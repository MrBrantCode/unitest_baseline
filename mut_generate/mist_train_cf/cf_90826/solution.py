"""
QUESTION:
Write a function named `calculate_standard_deviation` that takes an array of numbers as input and returns its standard deviation as a floating-point number with 2 decimal places. The array can contain up to 10^6 elements, including both positive and negative numbers. You cannot use built-in functions or libraries to calculate the standard deviation. The function should be efficient and have a time complexity of O(n), where n is the number of elements in the array. Assume the array will always have at least one element.
"""

import math

def calculate_standard_deviation(arr):
    n = len(arr)
    
    # Calculate the mean of the array
    mean = sum(arr) / n
    
    # Calculate the squared differences from the mean
    squared_diffs = [(x - mean)**2 for x in arr]
    
    # Calculate the variance
    variance = sum(squared_diffs) / n
    
    # Calculate the standard deviation
    std_dev = math.sqrt(variance)
    
    return round(std_dev, 2)