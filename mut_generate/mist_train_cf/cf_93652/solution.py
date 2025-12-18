"""
QUESTION:
Create a function called `binary_search` that takes in a sorted list of integers `lst` and a target item `item`. The function should return the index of the item if it exists in the list and -1 otherwise. The function must have a time complexity of O(log n), where n is the length of the list.
"""

def binary_search(lst, item):
    """
    This function performs a binary search on a sorted list of integers.
    
    Args:
        lst (list): A sorted list of integers.
        item (int): The target item to be searched.
    
    Returns:
        int: The index of the item if it exists in the list, -1 otherwise.
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