"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input and returns the index of the target value in the array. If the target value is not found, return -1. The function should have a time complexity of O(log n) to efficiently handle large arrays.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1