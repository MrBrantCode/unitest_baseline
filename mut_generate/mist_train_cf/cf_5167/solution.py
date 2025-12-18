"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list and a key value as input. The function should return the position of the key value in the list if it exists, with a time complexity of O(log n). If the key value is not found, return the error message "The key value '{}' is not found in the list." where '{}' is the key value.
"""

def binary_search(arr, key):
    """
    Perform binary search on a sorted list.

    Args:
        arr (list): A sorted list of elements.
        key: The value to search for in the list.

    Returns:
        int: The position of the key value in the list if it exists.
        str: An error message if the key value is not found in the list.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return f"The key value '{key}' is not found in the list."