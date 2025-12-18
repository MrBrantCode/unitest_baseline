"""
QUESTION:
Design a function named `binary_search` that takes two parameters: a sorted array of integers `arr` and a target value `target`. Return the index of the target value in the array if found, otherwise return -1. The array is guaranteed to be sorted in ascending order and may contain duplicates or be empty.
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