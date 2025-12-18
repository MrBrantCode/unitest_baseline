"""
QUESTION:
Write a function `binary_search_first_occurrence` that takes a sorted array of integers and a target integer as input, and returns the index of the first occurrence of the target element in the array. If the target element is not found, return -1. The function should have a time complexity of O(log n), where n is the size of the input array.
"""

def binary_search_first_occurrence(arr, target):
    """
    This function performs a binary search to find the index of the first occurrence 
    of a target element in a sorted array.

    Args:
    arr (list): A sorted list of integers.
    target (int): The target integer to be searched.

    Returns:
    int: The index of the first occurrence of the target element if found, -1 otherwise.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and (mid == 0 or arr[mid - 1] != target):
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1