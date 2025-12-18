"""
QUESTION:
Implement a function `binary_search(arr, target)` that takes a sorted array `arr` and a target number `target` as input, and returns the index of `target` if it exists in `arr`. If `target` is not found, return -1. The function must have a time complexity of O(log n).
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1