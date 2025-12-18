"""
QUESTION:
Implement a function named `binary_search` that takes two parameters: a sorted list `data` and a target value `target`. The function should perform a binary search to find the position of the `target` in the `data` list and return its index if found. If the `target` is not found, the function should return `None`. The function should also include error handling to catch `TypeError` exceptions that occur when the data types of the elements in the `data` set do not align with the `target`'s data type.
"""

def binary_search(data, target):
    """
    Perform a binary search to find the position of the target in the sorted data list.
    
    Args:
    data (list): A sorted list of elements.
    target: The target value to be searched in the data list.
    
    Returns:
    int or None: The index of the target if found, otherwise None.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid  # number found and return the position in list
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None  # number/word not found