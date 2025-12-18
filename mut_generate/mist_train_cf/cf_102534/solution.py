"""
QUESTION:
Implement a function `binary_search(arr, target)` that takes a sorted array `arr` and a target value `target` as input, and returns the index of the target value in the array. If the target value is not found, the function should return -1. Assume that the input array is already sorted in ascending order.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not present in the array
    return -1