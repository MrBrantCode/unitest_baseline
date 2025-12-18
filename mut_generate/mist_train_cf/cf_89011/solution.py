"""
QUESTION:
Write a function called `find_max_value` that takes an array as input and returns the maximum value in the array. You must implement the solution using a binary search algorithm and cannot use any built-in functions or methods for finding the maximum value, such as `max()` or `sort()`. The function should handle cases where the array is empty, has only one element, or is already sorted in non-descending order.
"""

def entance(arr):
    low = 0
    high = len(arr) - 1
    
    # Check if the array is empty
    if high < 0:
        return None
    
    # Check if the array has only one element
    if high == 0:
        return arr[0]
    
    # Check if the array is sorted in non-descending order
    if arr[low] <= arr[high]:
        return arr[high]
    
    # Perform binary search to find the maximum value
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the mid element is the maximum value
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return arr[mid]
        
        # Update the search range
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1
    
    return None  # In case the maximum value is not found