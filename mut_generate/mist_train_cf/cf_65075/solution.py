"""
QUESTION:
Write a function named `sort_subarrays` that sorts a given multi-dimensional array in ascending order. The sorting should be based on the sum of each sub-array elements. In case of a tie, sort based on the first element of the sub-array. The function should take a 2D list of integers as input and return a sorted 2D list of integers.
"""

def sort_subarrays(arr):
    """
    Sorts a given multi-dimensional array in ascending order based on the sum of each sub-array elements.
    In case of a tie, sort based on the first element of the sub-array.

    Args:
        arr (list): A 2D list of integers.

    Returns:
        list: A sorted 2D list of integers.
    """
    return sorted(arr, key=lambda x: (sum(x), x[0]))