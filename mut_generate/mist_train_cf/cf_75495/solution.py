"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input, and returns the index of the first occurrence of `target` in `arr` if it exists, or -1 otherwise. The function should not use any built-in search methods, and the array may contain duplicate values.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    first_occurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_occurrence = mid
            high = mid - 1  # continue the search in the lower half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_occurrence