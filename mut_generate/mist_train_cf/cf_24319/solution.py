"""
QUESTION:
Write a function `sort_array` that takes an array of integers as input and returns two arrays: one sorted in ascending order and the other sorted in descending order.
"""

def sort_array(arr):
    """
    This function takes an array of integers as input and returns two arrays: 
    one sorted in ascending order and the other sorted in descending order.

    Parameters:
    arr (list): The input list of integers.

    Returns:
    tuple: A tuple containing two lists. The first list is sorted in ascending order, 
    and the second list is sorted in descending order.
    """
    return sorted(arr), sorted(arr, reverse=True)