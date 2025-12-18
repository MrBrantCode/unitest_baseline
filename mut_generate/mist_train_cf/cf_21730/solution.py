"""
QUESTION:
Create a function `sort_even_less_than_five` that takes a list of integers as input. The function should return a new list containing the sum of each even number less than 5 and its square root rounded to the nearest whole number. The new list should be sorted in descending order. The time complexity of the solution should be O(nlogn), where n is the length of the input list.
"""

import math

def sort_even_less_than_five(numbers):
    """
    This function takes a list of integers, calculates the sum of each even number less than 5 
    and its square root rounded to the nearest whole number, then returns a new list in descending order.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A new list containing the sum of each even number less than 5 and its square root.
    """
    return sorted([math.isqrt(x) + x for x in numbers if x < 5 and x % 2 == 0], reverse=True)