"""
QUESTION:
Create a function called `transform_list` that takes a list of integers as input. The function should return a new list where all even numbers from the original list are doubled and all odd numbers are replaced with their square root rounded to the nearest integer.
"""

import math

def transform_list(nums):
    """
    This function takes a list of integers, doubles the even numbers, 
    and replaces the odd numbers with their square root rounded to the nearest integer.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A new list with the transformed numbers.
    """
    return [math.isqrt(num) if num % 2 != 0 else num * 2 for num in nums]