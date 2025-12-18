"""
QUESTION:
Implement a function `binary_search(arr, num)` that performs a binary search on a sorted array `arr` to find the index of the first occurrence of a specified integer `num`. If `num` is not found, return -1. The array may contain duplicate elements, and the function should be efficient for large arrays.
"""

def findFirst(arr, num):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            result = mid 
            right = mid - 1 
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return result