"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum contiguous subarray sum. The function must have a time complexity of O(n) and space complexity of O(1), without using any extra data structures.
"""

def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    curr_sum = arr[0]
    
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum