"""
QUESTION:
Implement a function named binary_search that uses the binary search technique to find the index of a target element x in a sorted array. The function should take four parameters: arr (the sorted array), low (the lowest index in the current search space), high (the highest index in the current search space), and x (the target element). The function should return the index of x if it is found, and -1 if it is not found.
"""

def binary_search(arr, low, high, x):
    """
    This function performs a binary search on a sorted array.

    Parameters:
    arr (list): The sorted array to search.
    low (int): The lowest index in the current search space.
    high (int): The highest index in the current search space.
    x (int): The target element to search for.

    Returns:
    int: The index of x if it is found, -1 otherwise.
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1