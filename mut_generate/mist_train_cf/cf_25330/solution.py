"""
QUESTION:
Implement a function named `search` that takes two parameters: a sorted list of integers (`array`) and a target integer (`target`). The function should return the index of the target in the array if found; otherwise, it should return -1. The function should have a time complexity of O(log n), where n is the number of elements in the array.
"""

def search(array, target):
    """
    Searches for a target integer in a sorted list of integers using binary search.
    
    Args:
    array (list): A sorted list of integers.
    target (int): The target integer to be searched.
    
    Returns:
    int: The index of the target in the array if found; otherwise, -1.
    """
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1