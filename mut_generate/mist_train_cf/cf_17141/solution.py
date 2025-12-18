"""
QUESTION:
Implement a function named `binary_search(arr, value)` that finds the position of a given value in a sorted array. The array is guaranteed to be sorted in ascending order. The function should have a time complexity of O(log n), where n is the length of the array. If the value is not found, the function should return -1.
"""

def binary_search(arr, value):
    """
    Finds the position of a given value in a sorted array using binary search.

    Args:
        arr (list): A sorted array of values.
        value: The value to search for.

    Returns:
        int: The position of the value if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1