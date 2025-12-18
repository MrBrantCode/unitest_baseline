"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find the index of the `target` value. The function should return the index of the `target` value if found, and -1 otherwise. The array is assumed to be sorted in ascending order.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found