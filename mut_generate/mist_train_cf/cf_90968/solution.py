"""
QUESTION:
Write a function `sort_descending` that takes an array of integers as input and returns the array sorted in descending order. The array can contain both positive and negative numbers.
"""

def sort_descending(arr):
    """
    Sorts the input array in descending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The input list sorted in descending order.
    """
    arr.sort(reverse=True)
    return arr