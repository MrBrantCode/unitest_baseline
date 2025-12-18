"""
QUESTION:
Write a function named `calculate_standard_deviation` that takes a list of integers as input and returns the standard deviation of the elements in the list. The standard deviation is calculated as the square root of the average of the squared differences from the mean. The average of the squared differences should be calculated by dividing by the length of the list minus one (Bessel's correction).
"""

import math

def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    
    squared_differences = [(x - mean)**2 for x in numbers]
    variance = sum(squared_differences) / (n - 1)
    
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation