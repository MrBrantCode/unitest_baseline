"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted 1D array of integers `arr` to find the index of the `target` value. The function should return the index of the target if it is present in the array, and -1 if it is not found. The array is assumed to be sorted in ascending order.
"""

def entrance(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found