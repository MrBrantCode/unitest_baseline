"""
QUESTION:
Write a function `smallest_subarray_with_sum` that takes an array of positive integers and a target sum as input, and returns the length of the smallest subarray with a sum greater than or equal to the target sum. If no such subarray exists, the function should return -1. The input array can contain duplicates and can be very large, with up to 10^6 elements. The target sum can be any positive integer up to 10^9.
"""

def smallest_subarray_with_sum(arr, target):
    smallest_length = float('inf')
    current_sum = 0
    window_start = 0
    
    for window_end in range(len(arr)):
        current_sum += arr[window_end]
        
        while current_sum >= target:
            smallest_length = min(smallest_length, window_end - window_start + 1)
            current_sum -= arr[window_start]
            window_start += 1
    
    return -1 if smallest_length == float('inf') else smallest_length