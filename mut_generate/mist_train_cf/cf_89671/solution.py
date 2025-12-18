"""
QUESTION:
Implement a function `binary_search(arr, target, low, high)` that performs a binary search on a sorted array to find the position of a target element. The array may contain duplicate elements and the function should return the position of the first occurrence of the target element if it appears multiple times. If the target element is not found, return -1. The function should be implemented recursively and have a time complexity of O(log n) and a space complexity of O(log n), where n is the size of the input array.
"""

def binary_search(arr, target, low, high):
    """
    Performs a binary search on a sorted array to find the position of a target element.
    
    Args:
    arr (list): A sorted list of elements.
    target: The target element to be found.
    low (int): The lower bound of the search range.
    high (int): The upper bound of the search range.
    
    Returns:
    int: The position of the first occurrence of the target element if found, -1 otherwise.
    """
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        if mid == 0 or arr[mid-1] != target:
            return mid
        else:
            return binary_search(arr, target, low, mid-1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)