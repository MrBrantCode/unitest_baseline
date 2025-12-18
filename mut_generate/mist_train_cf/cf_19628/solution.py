"""
QUESTION:
Implement a function `binary_search(arr, target)` that uses the binary search algorithm to find the index of a given `target` value in a sorted array `arr`. The function should return the index of the target value if found, and -1 if not found. The time complexity should be O(log n).
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