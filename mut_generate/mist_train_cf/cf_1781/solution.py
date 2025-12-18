"""
QUESTION:
Write a function max_subarray_sum that takes an array of integers as input and returns the maximum sum of a subarray that is non-empty, contiguous, has a length greater than or equal to 3, and consists only of positive integers.
"""

def entrance(arr):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            current_sum += arr[i]
            if current_sum > max_sum and i >= 2:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        else:
            current_sum = 0
    return max_sum