"""
QUESTION:
Implement a function `binary_search_descending` that searches for a specific item in a sorted array in descending order. The function should return the index of the target item if found, or -1 if not found. The array is guaranteed to be sorted in descending order.
"""

def binary_search_descending(arr, target):
    """
    Searches for a specific item in a sorted array in descending order.

    Args:
        arr (list): The sorted array in descending order.
        target: The item to be searched.

    Returns:
        int: The index of the target item if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            low = mid + 1
        else:
            high = mid - 1

    return -1