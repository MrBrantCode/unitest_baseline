"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array `arr` and a target element `target` as input and returns the index of the first occurrence of the target element in the array. If the target element is not found, return -1. The array is guaranteed to be non-empty and sorted.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # move left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result