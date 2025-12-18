"""
QUESTION:
Write a Python function `binary_search(arr, x)` that performs a binary search on a sorted array `arr` to find the index of the target element `x`. The function should return the index of `x` if found, or -1 if not found. Assume the input array is already sorted in ascending order. The function should have a time complexity of O(log n).
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