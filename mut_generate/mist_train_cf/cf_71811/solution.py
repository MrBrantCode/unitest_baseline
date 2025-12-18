"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input and returns the index of the target value in the array if found. If the target value is not found, return -1. Assume the array is 0-indexed and the input array is sorted in ascending order.
"""

def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the index of a target value.

    Args:
    arr (list): A sorted list of elements.
    target: The target value to be searched.

    Returns:
    int: The index of the target value if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1