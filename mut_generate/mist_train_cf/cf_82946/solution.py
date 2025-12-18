"""
QUESTION:
Create a function named `binary_search` that takes a sorted array and an item as input and returns the index of the item if found, otherwise returns -1. The function should have a time complexity of O(log n). The input array is sorted in ascending order, and the function should only consider the existing elements in the array.
"""

def binary_search(array, item):
    """
    Searches for an item in a sorted array using binary search.
    
    Args:
    array (list): A sorted list of items.
    item: The item to search for in the array.
    
    Returns:
    int: The index of the item if found, otherwise -1.
    """
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (start + end) // 2  # Find the middle element
        
        if array[mid] == item:  # Check if the middle element is the item
            return mid
        elif array[mid] > item:  # If middle element is greater, consider left half
            end = mid - 1
        else:  # If middle element is less, consider right half
            start = mid + 1
    
    return -1  # Return -1 if item not found