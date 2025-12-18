"""
QUESTION:
Implement a function `debug_program(arr)` that takes an array of integers as input and returns the index of the first element that is equal to its index, or -1 if no such element exists. The function should have a time complexity of O(n), a space complexity of O(1), and be able to handle arrays of any length and arrays with duplicate elements. The function should use a divide and conquer approach and not modify the input array.
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