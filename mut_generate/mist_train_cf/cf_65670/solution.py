"""
QUESTION:
Write a function named calculate_standard_deviation that takes a list of numbers as input and returns the standard deviation of the numbers in the list. The function should use the classic statistical formula, which involves calculating the mean, deviation from the mean, squared deviation, and the square root of the average of these squared deviations. The function should not use any built-in standard deviation functions.
"""

import math

def calculate_standard_deviation(num_array):
    mean = sum(num_array) / len(num_array)
    deviation = [x - mean for x in num_array]
    squared_deviation = [d ** 2 for d in deviation]
    average_squared_deviation = sum(squared_deviation) / len(squared_deviation)
    standard_deviation = math.sqrt(average_squared_deviation)
    return standard_deviation