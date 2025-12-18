"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find the index of the last occurrence of the target element. The array `arr` is sorted in ascending order and may contain duplicate elements. If the target element is not found, return -1. The function should handle the case where the target element appears multiple times in the array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result