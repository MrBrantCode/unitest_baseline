"""
QUESTION:
Write a function `smallest_subarray_with_sum(arr, target)` that takes an array of positive integers `arr` and a target sum `target` as input, and returns the length of the smallest subarray in `arr` that has a sum greater than or equal to `target`. If no such subarray exists, return -1. The input array can contain duplicates and can be very large with up to 10^6 elements, and the target sum can be any positive integer up to 10^9.
"""

def entance(nums, target):
    smallest_length = float('inf')
    current_sum = 0
    window_start = 0
    
    for window_end in range(len(nums)):
        current_sum += nums[window_end]
        
        while current_sum >= target:
            smallest_length = min(smallest_length, window_end - window_start + 1)
            
            current_sum -= nums[window_start]
            
            window_start += 1
    
    return -1 if smallest_length == float('inf') else smallest_length