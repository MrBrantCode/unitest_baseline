"""
QUESTION:
Implement a function named `interpolation_search` that takes a sorted array `arr` and a target value `target` as input and returns the index of the target value in the array if found, otherwise returns -1. The function should have a time complexity of O(log log n), where n is the size of the array.
"""

import math

def interpolation_search(arr, target):
    n = len(arr)
    start, end = 0, n-1
    while start <= end and arr[start] <= target <= arr[end]:
        mid = start + (end - start) * (target - arr[start]) // (arr[end] - arr[start])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1