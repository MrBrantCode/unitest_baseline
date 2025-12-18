"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum sum of a contiguous subarray. The function should have a time complexity of O(n) and assume the input array is not empty and contains at least one positive number.
"""

def max_subarray_sum(arr):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far