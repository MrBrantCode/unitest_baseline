"""
QUESTION:
Implement a function named `descendingOrder` that takes an array of integers as input and returns the array in descending order. The function should sort the input array in-place or create a new sorted array. The array may contain duplicate elements, and the function should return all elements in descending order.
"""

def descendingOrder(arr):
    """
    Returns the input array in descending order.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: A new array with the elements sorted in descending order.
    """
    return sorted(arr, reverse=True)