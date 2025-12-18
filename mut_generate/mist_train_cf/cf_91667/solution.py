"""
QUESTION:
Implement a function `search(arr, target)` that takes a sorted array `arr` and a target element `target` as input. The function should return the index of the first occurrence of `target` in `arr`. If `target` is not found, return -1. The function should have a time complexity of O(log n), where n is the size of `arr`.
"""

def search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching in the left half to find the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result