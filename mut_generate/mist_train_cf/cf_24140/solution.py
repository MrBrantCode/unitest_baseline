"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a contiguous subarray within the input array. The function should handle arrays with both positive and negative numbers.
"""

def max_subarray_sum(arr):
    max_sum = 0
    curr_sum = 0
    for x in arr:
        curr_sum += x
        if curr_sum < 0:
            curr_sum = 0
        elif curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum