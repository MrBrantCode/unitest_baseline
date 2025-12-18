"""
QUESTION:
Write a function `binary_search` that performs a recursive binary search on a sorted array. The function should take in the array, the low index, the high index, and the target element as parameters. It should return the index of the target element if found, or -1 if not found. The function should have a runtime complexity of O(log n). The input array is assumed to be sorted in ascending order.
"""

def binary_search(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1