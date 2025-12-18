"""
QUESTION:
Write a function `binary_search` that takes a sorted array `arr` and a target number `target` as input, and returns the index of the target number if found, or 'Not Found' otherwise. The array should be sorted in ascending order. The function should use a binary search algorithm.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'Not Found'