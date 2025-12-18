"""
QUESTION:
Implement a function named `binary_search` that takes two parameters: `arr` (a list of integers) and `x` (the target element). The function should sort the array first, then perform a binary search to find the index of the target element `x` in the sorted array. If the element is not found, return `-1`.
"""

def binary_search(arr, x):
    arr.sort()  # Sort the array first
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high:   
        mid = (high + low) // 2
  
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
  
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
  
        # If x is present at mid
        else:
            return mid
  
    # If element is not present
    return -1