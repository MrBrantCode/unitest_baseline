"""
QUESTION:
Write a function `transform_array` that takes an array of integers as input. Replace all odd numbers with 0 and all even numbers with their square root rounded to the nearest integer. Return the new array sorted in descending order.
"""

import math

def transform_array(arr):
    """
    Replaces all odd numbers in the input array with 0 and all even numbers with their square root rounded to the nearest integer.
    Returns the new array sorted in descending order.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The transformed array sorted in descending order.
    """
    return sorted([round(math.sqrt(num)) if num % 2 == 0 else 0 for num in arr], reverse=True)