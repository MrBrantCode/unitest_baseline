"""
QUESTION:
Implement a `search(arr, target)` function that uses binary search to find the index of a given `target` element in a sorted array `arr`. If the element is not present in the array, return -1. The input array is guaranteed to be sorted in ascending order.
"""

def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1