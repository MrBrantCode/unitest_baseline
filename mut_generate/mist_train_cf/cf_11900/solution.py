"""
QUESTION:
Implement a function `binary_search` that uses a binary search algorithm to find the index of the first occurrence of a given item in a sorted array with unique non-negative values. The function should have a time complexity of O(log n) and handle arrays with up to 10^6 elements.
"""

def binary_search(arr, item):
    """
    Uses binary search algorithm to find the index of the first occurrence of a given item in a sorted array with unique non-negative values.

    Args:
        arr (list): A sorted array with unique non-negative values.
        item (int): The item to search for in the array.

    Returns:
        int: The index of the first occurrence of the item if found, -1 otherwise.
    """
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == item:
            # Check if this is the first occurrence of the item
            if mid == 0 or arr[mid - 1] != item:
                return mid
            end = mid - 1
        elif arr[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1