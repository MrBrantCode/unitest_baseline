"""
QUESTION:
Write a binary search function that takes a sorted array and a target value as input, and returns the index of the target value in the array. The input array is guaranteed to be sorted in ascending order. The function should have a time complexity of O(log n), where n is the number of elements in the array.
"""

def binary_search(array, target):
    """
    Performs a binary search on a sorted array to find the index of the target value.

    Args:
    array (list): A sorted list of elements.
    target: The target value to search for.

    Returns:
    int: The index of the target value in the array, or -1 if not found.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1