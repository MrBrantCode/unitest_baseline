"""
QUESTION:
Implement a recursive binary search function, `binary_search`, that takes in a sorted array `arr`, the low index `low`, the high index `high`, and a target element `target`. The function should find the index of the target element in the array using a recursive approach and return -1 if the target element is not found. The function should have a runtime complexity of O(log n).
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