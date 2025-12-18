"""
QUESTION:
Write a function named max_subarray_sum that takes an array of integers as input and returns the maximum subarray sum that includes at least one negative number. The array may be empty. The function should return 0 for an empty array.
"""

def max_subarray_sum(arr):
    if not arr:
        return 0

    max_ending_here = 0
    max_so_far = float('-inf')

    for num in arr:
        max_ending_here += num

        if max_ending_here < 0:
            max_ending_here = 0

        if max_ending_here > max_so_far and any(x < 0 for x in arr):
            max_so_far = max_ending_here

    return max_so_far if max_so_far != float('-inf') else 0