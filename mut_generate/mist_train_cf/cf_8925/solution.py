"""
QUESTION:
Write a function `calculate_standard_deviation` that calculates the standard deviation of a list of integers. The standard deviation is calculated by finding the square root of the average of the squared differences from the mean. The function should take into account that the average of the squared differences should be divided by the length of the list minus one. The function should return the standard deviation of the input list.
"""

import math

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    
    squared_differences = [(x - mean)**2 for x in numbers]
    variance = sum(squared_differences) / (n - 1)
    
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation