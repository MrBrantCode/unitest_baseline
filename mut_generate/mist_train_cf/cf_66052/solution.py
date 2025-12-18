"""
QUESTION:
Implement a function `binary_search` that performs binary search on a numerically ordered array to find a specific entity. The function should take two parameters: a sorted array `arr` and the target entity `x`. It should return the index of the entity if found, and -1 otherwise. Assume the array is 0-indexed. Ensure the solution has optimal time and space complexity.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
  
    while low <= high:
        mid = (high + low) // 2
  
        # If entity is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
  
        # If entity is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
  
        # entity is present at the mid, return
        else:
            return mid 
  
    # Entity is not present in array
    return -1