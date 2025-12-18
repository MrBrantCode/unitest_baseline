"""
QUESTION:
Create a function `largest_subarray_sum` that takes an integer array `arr` as input and returns the largest sum of all possible subarray sums. The subarray must be contiguous, have a length of at least 3, and not include adjacent elements. The function should have a time complexity of O(n), where n is the length of the array.
"""

def largest_subarray_sum(arr):
    n = len(arr)
    
    if n < 3:
        return 0
    
    prev_max = arr[0]
    curr_max = max(arr[0], arr[1])
    
    for i in range(2, n):
        subarray_sum = max(prev_max + arr[i], curr_max)
        prev_max = curr_max
        curr_max = subarray_sum
    
    return max(prev_max, curr_max)