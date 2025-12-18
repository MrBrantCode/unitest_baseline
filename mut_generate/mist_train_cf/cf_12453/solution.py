"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array of strings `arr` to find the index of the first occurrence of the `target` string. The array can contain up to 1 million elements and may have duplicate strings. If the target string is not found, return -1.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            # Check if it's the first occurrence
            if mid == 0 or arr[mid-1] != target:
                return mid
            else:
                high = mid - 1
    
    return -1  # Target not found