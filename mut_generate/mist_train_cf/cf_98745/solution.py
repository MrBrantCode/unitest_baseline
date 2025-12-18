"""
QUESTION:
Write a function called `find_geometric_mean` that takes a list of 10 numbers as input, and returns the geometric mean of the three highest numbers in the list.
"""

import math

def find_geometric_mean(numbers):
    """
    This function calculates the geometric mean of the three highest numbers in a list.

    Parameters:
    numbers (list): A list of 10 numbers.

    Returns:
    float: The geometric mean of the three highest numbers in the list.
    """
    numbers.sort(reverse=True)
    highest_numbers = numbers[:3]
    product = 1
    for number in highest_numbers:
        product *= number
    return math.pow(product, 1/3)