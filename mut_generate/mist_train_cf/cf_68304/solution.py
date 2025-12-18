"""
QUESTION:
Write a function `multiply_abs_values(lst)` that takes a list of numbers as input and returns the product of the absolute values of the numbers, rounded down to the nearest integer, excluding any numbers above 100. The function should return the product of the remaining numbers.
"""

from math import prod, floor

def multiply_abs_values(lst):
    """
    This function takes a list of numbers as input, 
    and returns the product of the absolute values of the numbers, 
    rounded down to the nearest integer, excluding any numbers above 100.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The product of the absolute values of the numbers.
    """
    return prod(floor(abs(num)) for num in lst if num <= 100)