"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of integers `arr` and a target integer `target` as parameters. The function should return the index of the target in the list if found, otherwise return -1. The function must have a time complexity of O(log n) and a space complexity of O(1). Assume the input list `arr` is already sorted.
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