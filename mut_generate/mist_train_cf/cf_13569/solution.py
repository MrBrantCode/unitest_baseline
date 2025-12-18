"""
QUESTION:
Implement a function `calculate_std_dev` that takes a list of numbers as input and returns the standard deviation as a floating-point number. The result should be rounded to 2 decimal places and use "round half to even" rounding mode.
"""

import math

def calculate_std_dev(numbers):
    """
    This function calculates the standard deviation of a list of numbers.
    
    Args:
    numbers (list): A list of numbers.
    
    Returns:
    float: The standard deviation of the input numbers, rounded to 2 decimal places.
    """
    
    # First, we calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Then, we calculate the variance
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    # Finally, we calculate the standard deviation as the square root of the variance
    std_dev = math.sqrt(variance)
    
    # We round the result to 2 decimal places using the "round half to even" rounding mode
    std_dev = round(std_dev, 2)
    
    return std_dev