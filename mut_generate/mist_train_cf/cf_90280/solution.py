"""
QUESTION:
Implement a function `binary_search(arr, target)` that finds the index of a target value in a sorted array. The function should take two parameters: `arr` (a sorted array) and `target` (the value to be searched). If the target value is found, the function should return its index; otherwise, it should return -1. Assume the input array is already sorted in ascending order.
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