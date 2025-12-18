"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted list of integers `arr` to find the index of the `target` integer. If the `target` is not present in the list, the function should return -1.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1