"""
QUESTION:
Write a function `find_element(arr, target, index=0)` that returns the index of the first occurrence of `target` in the array `arr` using a recursive algorithm. If `target` is not found in `arr`, return -1. Assume `arr` only contains positive integers.
"""

def find_element(arr, target, index=0):
    """
    Returns the index of the first occurrence of target in the array arr using a recursive algorithm.
    
    Args:
        arr (list): A list of positive integers.
        target (int): The target number to be found.
        index (int, optional): The starting index for the search. Defaults to 0.

    Returns:
        int: The index of the first occurrence of target in arr. Returns -1 if target is not found.
    """
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return find_element(arr, target, index+1)