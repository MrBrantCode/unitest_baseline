"""
QUESTION:
Implement a `search` function that takes a sorted array `arr` and a target element `target` as input, and returns the index of the target element if found, or -1 if not found. The function should use binary search and have a time complexity of O(log n), where n is the size of the array.
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