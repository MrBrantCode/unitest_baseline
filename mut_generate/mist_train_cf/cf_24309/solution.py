"""
QUESTION:
Implement a function `sort_increasing_order` that sorts an array of numbers in ascending order. The function should return the sorted array.
"""

def sort_increasing_order(arr):
    """
    Sorts an array of numbers in ascending order.

    Args:
        arr (list): A list of numbers.

    Returns:
        list: The sorted list of numbers in ascending order.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_increasing_order(left) + middle + sort_increasing_order(right)