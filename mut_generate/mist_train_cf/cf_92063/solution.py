"""
QUESTION:
Write a function `find_greatest_number` that takes an array of integers (positive, negative, or zero) as input and returns the greatest number in the array. The array can contain any number of elements and may include duplicate values.
"""

def find_greatest_number(arr):
    """
    Returns the greatest number in the given array.

    Parameters:
    arr (list): A list of integers (positive, negative, or zero)

    Returns:
    int: The greatest number in the array
    """
    return max(arr)