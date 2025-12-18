"""
QUESTION:
Write a function called `binary_search_with_duplicates` that takes a sorted array `arr` and a target element `target` as input and returns the index of the first occurrence of the target element in the array. If the target element is not found, return -1. The function should be able to handle arrays of size up to 10^9 elements efficiently. The input array contains duplicate elements and is sorted in ascending order.
"""

def binary_search_with_duplicates(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Look for duplicates on the left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result