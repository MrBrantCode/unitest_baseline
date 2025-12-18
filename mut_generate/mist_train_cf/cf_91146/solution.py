"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a contiguous subarray. The array may contain both positive and negative numbers, and may be empty.
"""

def max_subarray_sum(arr):
    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far