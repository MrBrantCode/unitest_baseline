"""
QUESTION:
Write a function named `find_max_value` that takes an array of integers as input and returns the maximum value in the array without using built-in functions or methods for finding the maximum value. Implement the solution using a binary search algorithm to optimize the time complexity. The input array may be empty, contain one element, or be sorted in non-descending order. If the array is empty, the function should return None.
"""

def find_max_value(arr):
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
        if mid < high and arr[mid] > arr[mid + 1]:
            return arr[mid]
        
        # Update the search range
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1
    
    return None  # In case the maximum value is not found