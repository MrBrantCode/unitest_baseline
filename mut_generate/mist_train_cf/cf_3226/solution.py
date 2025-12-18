"""
QUESTION:
Write a function `binary_search_descending` that searches for a specific item in a sorted array in descending order. The function should return the index of the item if found, and -1 if not found. The time complexity should be O(log n) and space complexity should be O(1).
"""

def binary_search_descending(arr, target):
    """
    Searches for a specific item in a sorted array in descending order.
    
    Args:
    arr (list): A sorted list in descending order.
    target: The item to be searched.
    
    Returns:
    int: The index of the item if found, and -1 if not found.
    """
    
    # Initialize two pointers, left and right, to the first and last indices of the array
    left = 0
    right = len(arr) - 1
    
    # Continue the search until left is less than or equal to right
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the value at the middle index is equal to the target item, return the middle index
        if arr[mid] == target:
            return mid
        
        # If the value at the middle index is greater than the target item, update left to (middle + 1)
        elif arr[mid] > target:
            left = mid + 1
        
        # If the value at the middle index is less than the target item, update right to (middle - 1)
        else:
            right = mid - 1
    
    # If the target item is not found, return -1
    return -1