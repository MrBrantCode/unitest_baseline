"""
QUESTION:
Write a function named `sum_and_round` that calculates the sum of all integers in a given 2D array, ignoring non-integer elements, and returns the result rounded to the nearest whole number. The input array must have at least 3 nested lists, each containing at least 3 integers.
"""

import math

def sum_and_round(array):
    """
    This function calculates the sum of all integers in a given 2D array, 
    ignoring non-integer elements, and returns the result rounded to the nearest whole number.

    Args:
        array (list): A 2D array containing integers and/or non-integer elements.

    Returns:
        int: The sum of all integers in the array rounded to the nearest whole number.
    """
    total_sum = 0
    for sublist in array:
        for element in sublist:
            if isinstance(element, int):
                total_sum += element
    return round(total_sum)