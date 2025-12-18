"""
QUESTION:
Implement a function `binary_search_first_occurrence(arr, target)` that performs a binary search on a sorted array `arr` to find the index of the first occurrence of the `target` element. The array is guaranteed to be sorted in ascending order. If the target is not found, return -1.
"""

def binary_search_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Look for first occurrence on the left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result