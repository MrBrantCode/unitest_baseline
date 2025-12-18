"""
QUESTION:
Write a function `is_descending_order` that takes an array of integers as input and returns True if the array is sorted in descending order, False otherwise. The function should iterate through the array only once.
"""

def is_descending_order(arr):
    """
    Checks if an array is sorted in descending order.

    Args:
    arr (list): A list of integers.

    Returns:
    bool: True if the array is sorted in descending order, False otherwise.
    """
    is_sorted = True
    for i in range(1, len(arr)):
        if arr[i-1] <= arr[i]:
            is_sorted = False
            break
    return is_sorted