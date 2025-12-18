"""
QUESTION:
Implement the `binary_search` function, which takes a sorted array of integers `arr` and a target integer `target` as input, and returns the index of the first occurrence of `target` in `arr`. The array `arr` is sorted in ascending order and may contain duplicate elements. If `target` is not present in `arr`, return -1.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # look for first occurrence in the left half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result