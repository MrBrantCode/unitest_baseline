"""
QUESTION:
Write a function `find_max_index` that takes an array of at least 10 positive integers as input and returns the index of the maximum value in the array.
"""

def find_max_index(array):
    """
    This function finds the index of the maximum value in a given array.

    Parameters:
    array (list): A list of at least 10 positive integers.

    Returns:
    int: The index of the maximum value in the array.
    """
    return array.index(max(array))