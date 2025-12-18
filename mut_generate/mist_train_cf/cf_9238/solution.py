"""
QUESTION:
Write a function `find_index` that takes an array and a target value as input, and returns the index of the first occurrence of the target value in the array. If the target value is not found, return -1. The array can contain duplicate values.
"""

def find_index(arr, x):
    """
    Returns the index of the first occurrence of the target value in the array.
    
    Args:
    arr (list): The input array.
    x: The target value to be found.
    
    Returns:
    int: The index of the first occurrence of the target value. Returns -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1