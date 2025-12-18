"""
QUESTION:
Implement a function `max_subarray_sum` that finds the maximum sum of a subarray in an array of integers using dynamic programming with memoization. The function should handle arrays of size up to 10^6 and have a time complexity of O(n), where n is the size of the input array. The function should take an array of integers as input and return the maximum sum of a subarray.
"""

def max_subarray_sum(arr):
    max_so_far = float('-inf')  # Initialize with negative infinity
    max_ending_here = 0
    
    for num in arr:
        max_ending_here += num
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
            
    return max_so_far