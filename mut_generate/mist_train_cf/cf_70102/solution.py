"""
QUESTION:
Write a function called `sort_array_without_built_in` that takes an array of distinct integers as input and returns a new sorted array without using built-in sorting functions. The input array can be of any size, but the function should be designed with simplicity in mind, even if it's not the most efficient solution for large datasets.
"""

def sort_array_without_built_in(arr):
    """
    Sorts an array of distinct integers without using built-in sorting functions.

    Args:
        arr (list): A list of distinct integers.

    Returns:
        list: A new sorted list of integers.
    """
    new_arr = []
    arr_copy = arr[:]

    for _ in range(len(arr)):
        smallest = min(arr_copy)
        new_arr.append(smallest)
        arr_copy.remove(smallest)

    return new_arr