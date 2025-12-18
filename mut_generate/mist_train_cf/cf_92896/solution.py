"""
QUESTION:
Write a function `find_first_occurrence(arr, target)` that finds the index of the first occurrence of a given `target` element in a sorted array `arr` containing duplicate elements. The function should return the index of the first occurrence of the target element if found, or -1 otherwise.
"""

def find_first_occurrence(arr, target):
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