"""
QUESTION:
Write a function `binary_search_first_occurrence(arr, target)` that returns the index of the first occurrence of the target element in a sorted array `arr`. The array is sorted in ascending order. If the target element is not found, return -1. The function should have a time complexity of O(log n), where n is the size of the array.
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