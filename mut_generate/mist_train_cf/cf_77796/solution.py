"""
QUESTION:
Create a function called `sort_decreasing` that takes an array of integers as input and returns the array sorted in decreasing order. The function should use Python's built-in sorting functionality and must be able to handle arrays with any number of elements.
"""

def sort_decreasing(arr):
    """
    Sorts the input array in decreasing order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The input list sorted in decreasing order.
    """
    return sorted(arr, reverse=True)