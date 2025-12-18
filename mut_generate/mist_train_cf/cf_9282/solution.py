"""
QUESTION:
Create a function `calculate_standard_deviation(arr)` to calculate the standard deviation of an array of numbers with at least one element, handling both positive and negative numbers. The function should return the standard deviation as a floating-point number with 2 decimal places and have a time complexity of O(n), where n is the number of elements in the array. Do not use any built-in functions or libraries to calculate the standard deviation.
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