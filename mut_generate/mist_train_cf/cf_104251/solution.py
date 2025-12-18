"""
QUESTION:
Write a function `sum_array` that takes a list of floating-point numbers as input and returns the sum of all elements in the list rounded to the nearest integer. The list may contain negative numbers and non-integer values.
"""

from typing import List

def sum_array(arr: List[float]) -> int:
    """
    This function takes a list of floating-point numbers as input and returns 
    the sum of all elements in the list rounded to the nearest integer.
    
    Args:
        arr (List[float]): A list of floating-point numbers.
    
    Returns:
        int: The sum of all elements in the list rounded to the nearest integer.
    """
    return round(sum(arr))