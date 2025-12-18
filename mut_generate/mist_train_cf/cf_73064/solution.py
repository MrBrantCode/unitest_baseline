"""
QUESTION:
Implement a function called `binary_search(arr, target)` that takes a sorted array of integers and a target value as input. The function should return the index of the target value in the array if it exists, otherwise return -1. The function should use a binary search algorithm and have a time complexity of O(log N). The array indices should be integers, and the function should handle cases where the target value is less than the smallest value in the array.
"""

def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using binary search.

    Args:
    arr (list): A sorted list of integers.
    target (int): The target value to be searched.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # floor division

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1