"""
QUESTION:
Write a function `binary_search` that takes a target integer and a sorted list of integers as input and returns the index of the target if found, and -1 otherwise. The list can contain negative integers, zero, and positive integers. The function should use a recursive approach.
"""

def binary_search(target, array, start=0, end=None):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
        target (int): The target integer to be found.
        array (list): A sorted list of integers.
        start (int): The start index for the search. Defaults to 0.
        end (int): The end index for the search. Defaults to the last index of the array.

    Returns:
        int: The index of the target if found, -1 otherwise.
    """
    if end is None:
        end = len(array) - 1

    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(target, array, start, mid-1)
    else:
        return binary_search(target, array, mid+1, end)