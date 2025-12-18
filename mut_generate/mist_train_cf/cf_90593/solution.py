"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` of distinct positive integers and an integer `n` as input. The function should find the index of the first occurrence of `n` in `arr` if it exists, and return -1 otherwise. The function must have a time complexity of O(log n) and cannot use the built-in binary search function.
"""

def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == n:
            if mid > 0 and arr[mid-1] == n:
                high = mid - 1
            else:
                return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1