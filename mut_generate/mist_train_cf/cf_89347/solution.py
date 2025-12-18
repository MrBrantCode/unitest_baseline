"""
QUESTION:
Implement a function named `binary_search` that checks whether a given target element is present in a sorted array. The array is guaranteed to be sorted in ascending order, and the function should have a time complexity of O(log n), where n is the size of the array. The function should handle duplicate elements correctly, returning true only if at least one occurrence of the target element is present.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False