"""
QUESTION:
Implement a binary search algorithm with the function name `binary_search(arr, low, high, x)` that takes a sorted array `arr`, the lower index `low`, the upper index `high`, and the target element `x` as input, and returns the index of `x` in `arr` if found, otherwise -1. The algorithm should have a time complexity of O(log n) and a space complexity of O(log n).
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