"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find the index of the first occurrence of the target string `target`. If the target string is not found, return -1. The function should handle duplicate strings and have a time complexity of O(log n), where n is the number of elements in the array.
"""

def entance(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                high = mid - 1

    return -1