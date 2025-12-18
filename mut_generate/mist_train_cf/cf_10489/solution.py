"""
QUESTION:
Write a function named `binary_search` that takes in a sorted array `arr` and a target element `target` and returns the index of the `target` in `arr`. You may assume `arr` is sorted in ascending order. If `target` is not found, return -1.
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