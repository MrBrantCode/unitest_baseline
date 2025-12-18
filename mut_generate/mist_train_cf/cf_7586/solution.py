"""
QUESTION:
Write a recursive function `find_target_index` to find the index of the first occurrence of a target value in a sorted array. The function should take the array, the target value, and the start and end indices as parameters. If the target value is not found, return -1. The function should have a time complexity of O(log n).
"""

def find_target_index(arr, target, start, end):
    """
    Recursively find the index of the first occurrence of a target value in a sorted array.

    Args:
    arr (list): The input array, sorted in ascending order.
    target (int): The target value to be found.
    start (int): The start index of the current search range.
    end (int): The end index of the current search range.

    Returns:
    int: The index of the first occurrence of the target value if found, -1 otherwise.
    """
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return find_target_index(arr, target, start, mid - 1)
    
    else:
        return find_target_index(arr, target, mid + 1, end)