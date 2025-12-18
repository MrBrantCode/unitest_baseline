"""
QUESTION:
Implement a function binary_search that takes a sorted list of elements and a target element as input and returns the index of the target element if found, or -1 if not found. The function should use a divide and conquer approach and have a time complexity of O(log n), where n is the number of elements in the list. The list is 0-indexed and the function should be able to handle duplicate elements.
"""

def binary_search(arr, target):
    """
    Searches for a target element in a sorted list using binary search.

    Args:
        arr (list): A sorted list of elements.
        target: The target element to be searched.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1