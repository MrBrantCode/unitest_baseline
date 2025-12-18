"""
QUESTION:
Write a recursive binary search function, `binary_search(arr, target, low, high)`, that takes a sorted array `arr` in ascending order, a target element `target`, and the indices `low` and `high` as input, and returns the position of the first occurrence of the target element if found, otherwise returns -1.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        if mid == 0 or arr[mid - 1] != target:
            return mid
        else:
            return binary_search(arr, target, low, mid - 1)
    
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    
    else:
        return binary_search(arr, target, low, mid - 1)