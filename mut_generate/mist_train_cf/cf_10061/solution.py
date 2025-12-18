"""
QUESTION:
Write a function `find_max_index` that takes a list of at least 10 positive integers as input and returns the index of the maximum value in the list.
"""

def find_max_index(array):
    """
    This function finds the index of the maximum value in a list of integers.

    Args:
        array (list): A list of at least 10 positive integers.

    Returns:
        int: The index of the maximum value in the list.
    """
    return array.index(max(array))