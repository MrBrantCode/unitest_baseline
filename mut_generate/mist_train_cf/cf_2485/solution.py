"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array to find the index of the first occurrence of the target element. If the target element is not found, return the index of the next smallest element in the array. The input array will be sorted and will not be empty, and the function should return an integer value.
"""

def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the index of the first occurrence of the target element.
    If the target element is not found, return the index of the next smallest element in the array.

    Args:
        arr (list): A sorted list of elements.
        target: The target element to search for.

    Returns:
        int: The index of the first occurrence of the target element, or the index of the next smallest element if not found.
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if result == -1:
        return right + 1
    else:
        return result