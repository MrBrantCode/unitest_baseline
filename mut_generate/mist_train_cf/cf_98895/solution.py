"""
QUESTION:
Implement a function `interpolation_search(arr, target)` that performs an interpolation search on a sorted array `arr` to find the index of the `target` value. The function should return the index of the `target` value if it exists in the array, and -1 otherwise. The search should be performed in O(log log n) time complexity. The array `arr` is sorted in ascending order and may contain duplicate elements.
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