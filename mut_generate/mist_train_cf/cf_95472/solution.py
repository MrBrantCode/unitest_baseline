"""
QUESTION:
Define a function `search_recursive(arr, target, start=0)` that takes an array `arr`, a target element `target`, and an optional starting index `start` (defaulting to 0) as input. The function should search for the first occurrence of `target` in `arr` and return its index if found; otherwise, it should return -1. The array may be unsorted and can contain duplicate elements. Implement the function using a recursive approach.
"""

def entrance(arr, target, start=0):
    if start == len(arr):
        return -1

    if arr[start] == target:
        return start

    return entrance(arr, target, start+1)