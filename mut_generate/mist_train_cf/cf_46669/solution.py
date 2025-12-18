"""
QUESTION:
Create a function named `array_sort` that takes an array of integers as input and returns the array with its elements in ascending order. The function should not modify the original array. If an in-place solution is also desired, create a function named `array_sort_in_place` that sorts the array in ascending order without creating a new array.
"""

def array_sort(arr):
    """
    Returns a new sorted array in ascending order without modifying the original array.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: A new sorted array in ascending order.
    """
    return sorted(arr)


def array_sort_in_place(arr):
    """
    Sorts the array in ascending order in-place without creating a new array.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: The sorted array in ascending order.
    """
    arr.sort()
    return arr