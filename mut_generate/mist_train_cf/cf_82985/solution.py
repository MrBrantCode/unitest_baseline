"""
QUESTION:
Write a function `binary_search(arr, low, high, x)` that takes a sorted array `arr`, its lowest index `low`, highest index `high`, and a target element `x`, and returns the index of `x` if it exists in `arr`. If `x` is present more than once, any of its occurrences can be returned. If `x` does not exist, return -1. Assume that the array elements may not be unique.
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1