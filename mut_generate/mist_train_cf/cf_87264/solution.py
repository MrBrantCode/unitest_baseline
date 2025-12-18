"""
QUESTION:
Create a function named `round_sum` that takes an array of numbers as input and returns the sum of all elements in the array rounded to the nearest integer. The array may contain negative numbers, floating-point numbers, and complex numbers. If the array contains complex numbers, only the real part of the complex number should be included in the sum. The time complexity of the function should be O(n), where n is the number of elements in the array.
"""

import math

def round_sum(arr):
    """
    Calculate the sum of all elements in the array, 
    rounded to the nearest integer.

    If the array contains complex numbers, only the real part 
    of the complex number is included in the sum.

    The time complexity of the function is O(n), where n is the 
    number of elements in the array.

    Parameters:
    arr (list): A list of numbers that may include negative numbers, 
                floating-point numbers, and complex numbers.

    Returns:
    int: The sum of all elements in the array rounded to the nearest integer.
    """
    total = 0
    for num in arr:
        if isinstance(num, complex):
            total += num.real
        else:
            total += num

    return round(total)