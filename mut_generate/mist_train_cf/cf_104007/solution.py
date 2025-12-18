"""
QUESTION:
Write a function `binary_search` that takes a sorted array `arr` and an integer `n` as parameters. The function should return the index of the first occurrence of `n` in the array if it is present, otherwise return -1. The time complexity of the function should be O(log n).
"""

def binary_search(arr, n):
    """
    This function performs a binary search on a sorted array to find the index of the first occurrence of a given integer.
    
    Parameters:
    arr (list): A sorted list of integers.
    n (int): The integer to be searched in the list.
    
    Returns:
    int: The index of the first occurrence of n in the array if it is present, otherwise -1.
    """
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return -1