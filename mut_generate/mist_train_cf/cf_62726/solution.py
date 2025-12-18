"""
QUESTION:
Write a function `max_subarray_sum` that calculates the maximum sum of a contiguous subarray within a given numerical array. The function should handle large input sizes (n > 10^5), floating point numbers, and negative numbers, with a time complexity of O(n log n) or better.
"""

def max_subarray_sum(arr):
    size = len(arr)
  
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0   
    return max_so_far