"""
QUESTION:
Design a function `ternary_search(arr, l, r, x)` to perform ternary search on a sorted array of integers. The function should take as input the array `arr`, the starting index `l`, the ending index `r`, and the target element `x`. It should return the index of `x` if found, and -1 otherwise. The function should handle edge cases where the array is empty or contains duplicate integers.
"""

def ternary_search(arr, l, r, x):
    if r >= l: 
        mid1 = l + (r-l) // 3
        mid2 = mid1 + (r-l) // 3
  
        if arr[mid1] == x: 
            return mid1 
  
        if arr[mid2] == x: 
            return mid2  
  
        if arr[mid1] > x: 
            return ternary_search(arr, l, mid1-1, x) 
  
        if arr[mid2] < x: 
            return ternary_search(arr, mid2 + 1, r, x) 
  
        return ternary_search(arr, mid1 + 1, mid2 - 1, x) 
    return -1