"""
QUESTION:
Create a function named `binary_search` that takes a sorted array `arr` and a target number `target` as input. Implement a binary search algorithm to find the index of `target` in `arr`. If `target` is found, return its index; otherwise, return -1. The array `arr` is sorted in ascending order using the merge sort algorithm.
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