"""
QUESTION:
Write a function `calculate_std_dev` that takes a list of numeric values as input and returns their population standard deviation as a floating-point number. The function should compute the average of the input values, calculate the variance, and return the square root of the variance. The variance should be calculated by dividing the sum of the squared differences from the average by the total number of values.
"""

import math

def calculate_std_dev(numbers):
    # Compute the average
    average = sum(numbers) / len(numbers)
    
    # Compute the sum of square differences from the average
    sum_of_square_diffs = sum((num - average) ** 2 for num in numbers)
    
    # Compute the variance (average of the squared differences)
    variance = sum_of_square_diffs / len(numbers)
    
    # The standard deviation is the square root of the variance
    return math.sqrt(variance)