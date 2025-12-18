"""
QUESTION:
Implement a function `binary_search(arr, low, high, x)` that performs a binary search on a sorted array `arr` to find the index of the element `x`. The function should return the index of `x` if found, and -1 if `x` is not present in the array. The space complexity of the function should not exceed O(n).
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