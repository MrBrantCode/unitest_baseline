"""
QUESTION:
Write a function named `find_max_index` that takes an array of integers as input and returns the index of the maximum value in the array. Assume the input array contains at least one element and may contain duplicate values, in which case the function should return the index of the first occurrence of the maximum value. The function should use 0-based indexing.
"""

def find_max_index(array):
    """
    Returns the index of the maximum value in the array.

    Args:
        array (list): A list of integers.

    Returns:
        int: The index of the maximum value in the array.
    """
    return array.index(max(array))