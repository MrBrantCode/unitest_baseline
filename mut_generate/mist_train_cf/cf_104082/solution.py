"""
QUESTION:
Implement a function `binary_search(arr, x)` that performs a binary search on the input array `arr` to find the index of the target element `x`. The input array `arr` is sorted in ascending order. The function should return the index of `x` if it exists in the array, otherwise return -1. The function must use a binary search algorithm with a step size of 1 for updating the low and high indices.
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