"""
QUESTION:
Implement a function `binary_search(arr, low, high, x)` to locate an element `x` within a chronologically ordered array `arr` using binary search technique. The function should return the index of `x` if found, otherwise return -1. The function should take four parameters: `arr` (the chronologically ordered array), `low` and `high` (the extremities of the array or subarray), and `x` (the element to be located).
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