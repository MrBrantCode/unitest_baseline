"""
QUESTION:
Create a function `last_occurrence` that takes a sorted array `arr` and a target number `target` as input. The function should return the index of the last occurrence of `target` in `arr`. If `target` does not exist in `arr`, return -1. The function should have a time complexity of O(log n).
"""

def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result