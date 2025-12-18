"""
QUESTION:
Create a function `binary_search(arr, target)` that searches for a given number `target` in a sorted array `arr`. The function should return the index of the first occurrence of `target` if it exists in `arr`, or -1 if it does not. The function should have a time complexity of O(log n), where n is the length of `arr`, and should be able to handle large input arrays efficiently. If `arr` contains duplicate elements, the function should return the index of the leftmost occurrence of `target`.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result