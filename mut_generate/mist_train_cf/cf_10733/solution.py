"""
QUESTION:
Implement a function `binary_search` that takes a sorted list `data`, a target number `target`, and indices `low` and `high` as input. The function should return the index of the first occurrence of the `target` in the `data` list using a recursive binary search algorithm. If the `target` is not found, the function should return -1. The function should have a time complexity of O(log n), where n is the size of the `data` list.
"""

def binary_search(data, target, low, high):
    """
    Recursive binary search function to find the index of the first occurrence of the target in a sorted list.

    Args:
    data (list): A sorted list of numbers.
    target (int): The target number to be searched.
    low (int): The starting index of the current search range.
    high (int): The ending index of the current search range.

    Returns:
    int: The index of the first occurrence of the target if found, -1 otherwise.
    """
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if data[mid] == target:
        if mid == 0 or data[mid - 1] != target:
            return mid
        else:
            return binary_search(data, target, low, mid - 1)
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, high)
    else:
        return binary_search(data, target, low, mid - 1)