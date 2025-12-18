"""
QUESTION:
Implement a function named `binary_search` that takes in two parameters: a sorted list of integers `data` and a target integer `target`. The function should return the index of the `target` in the `data` list if it exists, otherwise return -1. The function must use the binary search algorithm and the input list is assumed to be sorted in ascending order.
"""

def binary_search(data, target):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
    data (list): A sorted list of integers.
    target (int): The target integer to be searched.
    
    Returns:
    int: The index of the target in the data list if it exists, otherwise -1.
    """
    
    low = 0
    high = len(data) - 1
    
    while low <= high:
        index = (low + high) // 2
        value = data[index]

        if value == target:
            return index

        if target < value:
            high = index - 1
        else:
            low = index + 1

    return -1