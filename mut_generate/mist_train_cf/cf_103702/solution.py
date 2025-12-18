"""
QUESTION:
Write a function `find_first_occurrence(arr, target)` that returns the index of the first occurrence of a given target element in a sorted array `arr` with duplicate elements. The array is 0-indexed and may contain negative numbers. If the target is not found, return -1. Assume that the input array is sorted in ascending order.
"""

def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result