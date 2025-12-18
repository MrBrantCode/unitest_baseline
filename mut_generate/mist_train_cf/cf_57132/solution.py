"""
QUESTION:
Write a function named `linear_search` that takes an array `arr` and a value `x` as input. Return the index of `x` in `arr` if it is present; otherwise, return -1.
"""

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1