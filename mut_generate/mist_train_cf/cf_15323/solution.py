"""
QUESTION:
Create a function called `binary_search` that takes a sorted list of integers and a target item as input, and returns the index of the target item if it exists in the list, and -1 otherwise. The function should have a time complexity of O(log n), where n is the length of the list. The input list is sorted in ascending order.
"""

def binary_search(lst, item):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
    lst (list): A sorted list of integers.
    item (int): The target item to be searched.
    
    Returns:
    int: The index of the target item if it exists, -1 otherwise.
    """
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == item:
            return mid
        elif item < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1