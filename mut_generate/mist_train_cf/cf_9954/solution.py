"""
QUESTION:
Find the maximum contiguous subarray sum in an array of integers that may contain both positive and negative numbers, including the possibility of an empty array. Implement the function `max_subarray_sum(arr)` to solve this problem, where `arr` is the input array. The function should return the maximum subarray sum.
"""

def max_subarray_sum(arr):
    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far