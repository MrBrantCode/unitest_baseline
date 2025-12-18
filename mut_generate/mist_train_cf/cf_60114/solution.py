"""
QUESTION:
Write a function `linear_search(arr, x)` that takes an unsorted array `arr` and a target value `x` as input, and returns the index of `x` if found in `arr`, or a message indicating that `x` is not found. The function should handle cases where `x` is not present in `arr`.
"""

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "Element not found"