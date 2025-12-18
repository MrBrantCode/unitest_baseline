"""
QUESTION:
Write a function `calculate_geometric_mean` that takes a list of 10 numbers and returns the geometric mean of the three highest numbers. The function should not take any other parameters.
"""

import math

def calculate_geometric_mean(numbers):
    """
    Calculate the geometric mean of the three highest numbers in a list.
    
    Parameters:
    numbers (list): A list of 10 numbers.
    
    Returns:
    float: The geometric mean of the three highest numbers.
    """
    numbers.sort(reverse=True)
    highest_numbers = numbers[:3]
    product = 1
    for number in highest_numbers:
        product *= number
    return math.pow(product, 1/3)