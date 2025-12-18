"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array and a target value as input. The function should return the index of the smallest element in the array that is greater than the target value. If no such element exists, return -1. The array is sorted in ascending order.
"""

def binary_search(array, target):
    """
    This function performs a binary search to find the index of the smallest element 
    in a sorted array that is greater than the target value. If no such element exists, 
    it returns -1.

    Parameters:
    array (list): A sorted list of elements.
    target (int): The target value.

    Returns:
    int: The index of the smallest element greater than the target value.
    """

    left = 0
    right = len(array) - 1
    result_index = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] > target:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return result_index