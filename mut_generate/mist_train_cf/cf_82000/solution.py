"""
QUESTION:
Write a function called `find_max_index` that takes an array of integers as input and returns the index of the maximum value in the array. The function must work with 0-based indexing.
"""

def find_max_index(arr):
    """
    This function finds the index of the maximum value in an array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The index of the maximum value in the array.
    """
    max_value = max(arr)
    index = arr.index(max_value)
    return index