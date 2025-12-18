"""
QUESTION:
Implement a function named `binary_search` that takes two parameters: a sorted list of distinct integers `arr` with at most 1,000,000 elements and a target integer `target`. The function should return the index of `target` in `arr` if found, and -1 otherwise.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1