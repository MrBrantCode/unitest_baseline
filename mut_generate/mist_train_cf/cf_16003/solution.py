"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array and a target number as input, and returns the index of the target number in the array if found, or -1 if not found. The array contains 1000 integers, each ranging from 1 to 1000000, and is sorted in ascending order.
"""

def binary_search(arr, target):
    """
    Searches for a target number in a sorted array using binary search.

    Args:
    arr (list): A sorted list of integers.
    target (int): The target number to be searched.

    Returns:
    int: The index of the target number if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1