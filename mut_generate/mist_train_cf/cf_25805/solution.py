"""
QUESTION:
Write a function `calculate_standard_deviation` that calculates the standard deviation of a given array of numbers. The function should take a list of numbers as input and return the standard deviation as a floating-point number. The standard deviation should be calculated using the formula: σ = √((∑(x - mean)^2)/n), where σ is the standard deviation, x represents each number in the list, mean is the average of the numbers, and n is the count of numbers.
"""

import math

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a given array of numbers.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        float: The standard deviation of the input numbers.
    """
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)