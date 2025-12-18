"""
QUESTION:
Implement a function `binary_search(arr, x)` that performs a binary search for an element `x` in a sorted array `arr`. The function should return the index of `x` if found, or -1 if not found. The array `arr` is sorted in ascending order.
"""

def entance(arr, x): 
    low = 0
    high = len(arr) - 1
    while low <= high: 
        mid = (high+low)//2
        if arr[mid] < x: 
            low = mid + 1
        elif arr[mid] > x: 
            high = mid - 1
        else: 
            return mid 
  
    return -1