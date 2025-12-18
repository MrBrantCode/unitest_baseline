"""
QUESTION:
Implement a function called `find_index` that takes an array `arr` and an `item` as input, and returns the index of the first occurrence of `item` in `arr`. If `item` is not found in `arr`, return -1. The solution should not use any built-in functions or libraries that directly solve the problem.
"""

def find_index(arr, item):
    """
    Returns the index of the first occurrence of item in arr.
    Returns -1 if item is not found in arr.

    :param arr: The array to search in
    :param item: The item to search for
    :return: The index of the first occurrence of item in arr, or -1 if not found
    """
    index = -1
    for i in range(len(arr)):
        if arr[i] == item:
            index = i
            break
    return index