"""
QUESTION:
Create a function named `sort_even_squares` that takes a list of integers as input. The function should return a new list containing the square root of even numbers less than 5 from the original list, rounded to the nearest whole number. The new list should be sorted in descending order.
"""

import math

def sort_even_squares(nums):
    """
    Returns a new list containing the square root of even numbers less than 5 from the input list,
    rounded to the nearest whole number. The new list is sorted in descending order.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of integers.
    """
    return sorted([math.isqrt(num) for num in nums if num < 5 and num % 2 == 0], reverse=True)