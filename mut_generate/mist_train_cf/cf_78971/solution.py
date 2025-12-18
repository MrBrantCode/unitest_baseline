"""
QUESTION:
Design a function `binary_search` that takes a sorted array 'arr' in ascending order and a target value 'key' as input, and returns the index of 'key' in the array 'arr'. If 'key' doesn't exist, return -1. Assume all elements in the array are distinct.
"""

def binary_search(arr, key):
    """
    Searches for a target value 'key' in a sorted array 'arr' using binary search.
    
    Args:
        arr (list): A sorted list of distinct elements in ascending order.
        key: The target value to be searched in the list.
    
    Returns:
        int: The index of 'key' in 'arr' if found, -1 otherwise.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1