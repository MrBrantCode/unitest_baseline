"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` and a target element `target` as input, and returns the index of the first occurrence of the target element in the array. If the target element is not found, return -1. The array is sorted in non-decreasing order.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if low < len(arr) and arr[low] == target:
        return low

    return -1