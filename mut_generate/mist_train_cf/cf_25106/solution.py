"""
QUESTION:
Write a function `find_largest_index` that takes an array of integers as input and returns the index of the largest element in the array. The array contains at least one element.
"""

def find_largest_index(arr):
    """
    This function finds the index of the largest element in a given array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The index of the largest element in the array.
    """
    largest_element = max(arr)
    return arr.index(largest_element)