"""
QUESTION:
Implement the `binary_search(arr, x)` function to find the index of a target value `x` in a sorted array `arr`. The function should return the index of `x` if found, and -1 if not found. The array `arr` is guaranteed to be sorted in ascending order.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
 
    return -1