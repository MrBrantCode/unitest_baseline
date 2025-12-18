"""
QUESTION:
Implement a binary search operation on a list of even numbers from 2 to 100 and analyze its time complexity. The binary search function should take the list and a target number as input and return the index of the target number if found, or -1 if not found. The input list is already sorted in ascending order.
"""

def entrance(arr, target):
    """
    Performs binary search on a sorted list and returns the index of the target number.
    
    Parameters:
    arr (list): A sorted list of numbers.
    target (int): The target number to search for.
    
    Returns:
    int: The index of the target number if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1