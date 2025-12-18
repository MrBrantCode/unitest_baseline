"""
QUESTION:
Write a function, named `sort_descending`, that takes an array of integers as input and returns the array sorted in descending order.
"""

def sort_descending(arr):
    """
    This function takes an array of integers as input and returns the array sorted in descending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The input list sorted in descending order.
    """
    return sorted(arr, reverse=True)