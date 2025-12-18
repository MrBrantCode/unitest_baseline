"""
QUESTION:
Write a function `update_third_element` that takes an array of integers as input and returns a new value for the third element of the array. The new value should be greater than 10 and should be calculated using only bitwise operations. The original array should remain unchanged.
"""

def update_third_element(arr):
    """
    This function takes an array of integers as input, calculates a new value for the third element 
    using only bitwise operations and returns the new value. The new value is greater than 10.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The new value for the third element.
    """
    return arr[2] | 16