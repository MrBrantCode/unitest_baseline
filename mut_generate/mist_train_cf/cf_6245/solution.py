"""
QUESTION:
Write a function `update_third_element` that takes an array of integers as input and returns the value of the third element changed to be greater than 100 using only bitwise shift operations. The original array should remain unchanged.
"""

def update_third_element(arr):
    """
    This function takes an array of integers as input and returns the value of the third element changed to be greater than 100 using only bitwise shift operations.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The value of the third element changed to be greater than 100.
    """
    return arr[2] | (1 << 7)