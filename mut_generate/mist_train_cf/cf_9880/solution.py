"""
QUESTION:
Implement a function named `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a subarray within the array. The function should have a time complexity of O(n), where n is the size of the input array, and be able to handle arrays of size up to 10^6.
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