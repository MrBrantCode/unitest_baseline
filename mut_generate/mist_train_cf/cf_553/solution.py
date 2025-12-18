"""
QUESTION:
Write a function `calculate_standard_deviation` that calculates the standard deviation of an array of unique numbers with a time complexity of O(n), where n is the number of elements in the array. The function should return the standard deviation as a floating-point number with 6 decimal places. It should also validate that the input array contains only unique elements and return an error message if the array contains duplicate elements. The input array can contain up to 10^9 elements and can have both positive and negative numbers.
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