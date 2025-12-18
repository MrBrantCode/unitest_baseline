"""
QUESTION:
Create a function `calculate_standard_deviation(arr)` to calculate the standard deviation of an array of numbers. The array can contain up to 10^9 elements, may include both positive and negative numbers, and must contain only unique elements. The function should return the standard deviation as a floating-point number with 6 decimal places and have a time complexity of O(n), where n is the number of elements in the array. Do not use any built-in functions or libraries to calculate the standard deviation.
"""

import math

def calculate_standard_deviation(arr):
    n = len(arr)
    
    # Validate unique elements in the array
    if len(set(arr)) != n:
        return "Error: Input array must contain only unique elements."
    
    # Calculate the mean
    mean = sum(arr) / n
    
    # Calculate the sum of squares
    sum_of_squares = sum((x - mean) ** 2 for x in arr)
    
    # Calculate the variance
    variance = sum_of_squares / n
    
    # Calculate the standard deviation
    std_deviation = math.sqrt(variance)
    
    return round(std_deviation, 6)