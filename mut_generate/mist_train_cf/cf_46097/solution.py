"""
QUESTION:
Implement a function `binary_search` that performs a binary search on a sorted array to find a given number. The function should take two parameters: a sorted array `arr` and a number `x` to search for. It should return the index of the number if found, otherwise return -1. Assume the array may contain negative numbers and duplicates. The function should handle cases when the given number does not exist in the array.
"""

def binary_search(arr, x):
    """
    Performs a binary search on a sorted array to find a given number.

    Args:
        arr (list): A sorted array of numbers.
        x (int): The number to search for in the array.

    Returns:
        int: The index of the number if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1