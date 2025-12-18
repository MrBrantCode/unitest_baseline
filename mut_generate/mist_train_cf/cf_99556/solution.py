"""
QUESTION:
Implement a function `binary_search` that takes a sorted array of integers `arr` and a target integer `target` as input, and returns the index of `target` in `arr` if found, or -1 if not found. The function should use the binary search algorithm. The input array is sorted in ascending order.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1