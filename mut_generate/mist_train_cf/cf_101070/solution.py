"""
QUESTION:
Write a function `find_geometric_mean` that takes a list of exactly 10 numbers as input, returns the geometric mean of the three largest numbers in the list.
"""

import math

def find_geometric_mean(numbers):
    """
    This function calculates the geometric mean of the three largest numbers in a list of exactly 10 numbers.
    
    Args:
        numbers (list): A list of exactly 10 numbers.
    
    Returns:
        float: The geometric mean of the three largest numbers in the list.
    """
    
    # Sort the list in descending order
    numbers.sort(reverse=True)
    # Take the first three numbers from the sorted list
    highest_numbers = numbers[:3]
    # Calculate the geometric mean of the three highest numbers
    product = 1
    for number in highest_numbers:
        product *= number
    geometric_mean = math.pow(product, 1/3)
    return geometric_mean