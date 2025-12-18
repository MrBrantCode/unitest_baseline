"""
QUESTION:
Given a sorted array of integers, write a function `debug_program` that finds the index of an element that is equal to its index in the array, if such an element exists. If no such element exists, return -1. The function should handle arrays with duplicate elements and have a time complexity of O(n) and a space complexity of O(1).
"""

def debug_program(arr):
    n = len(arr)
    return binary_search(arr, 0, n - 1)

def binary_search(arr, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == mid:
        return mid
    
    left_result = binary_search(arr, start, min(mid - 1, arr[mid]))
    right_result = binary_search(arr, max(mid + 1, arr[mid]), end)
    
    return max(left_result, right_result)