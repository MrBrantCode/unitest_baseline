"""
QUESTION:
Implement a function `binary_search(arr, x)` that takes a sorted array `arr` and a target value `x` as input and returns the index of `x` in the array if found, or -1 if not found. The array is expected to be sorted in non-decreasing order. The function should achieve a time complexity of O(log n) and should not use any built-in Python functions or libraries.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1