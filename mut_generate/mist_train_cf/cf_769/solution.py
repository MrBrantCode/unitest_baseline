"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted list of integers `arr` to find the index of the `target` integer. If the `target` is not found, the function should return -1. The function should have a time complexity of O(log n) and a space complexity of O(1), and it should not use any built-in sorting or searching functions.
"""

def binary_search(arr, target):
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

    return -1