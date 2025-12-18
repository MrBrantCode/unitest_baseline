"""
QUESTION:
Implement a function `binary_search(arr, x)` that performs a binary search on a sorted array `arr` to find the index of a target element `x`. The function should return the index of `x` if it exists in the array, and -1 otherwise. The array is sorted in ascending order and can contain duplicate elements.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1