"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array `arr` and a target value `x` as input, and returns the index of `x` in `arr` if it exists, or -1 otherwise. The array can have up to 1 million elements.
"""

def binary_search(arr, x): 
    l = 0
    r = len(arr) - 1

    while l <= r: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
  
    return -1