"""
QUESTION:
Implement a function named `binary_search` that takes a sorted one-dimensional array `arr` and a target element `target` as input and returns the index of the first occurrence of the target element. The function should handle duplicate values in the array and should not use any inbuilt Python library methods for binary search.
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