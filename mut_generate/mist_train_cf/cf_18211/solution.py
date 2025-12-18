"""
QUESTION:
Write a function named `find_max_consecutive_subarrays` that takes an array `arr` and a target sum as input, and returns the maximum number of consecutive subarrays with a sum equal to the target sum, given that each subarray must have a minimum length of 4.
"""

def find_max_consecutive_subarrays(arr, target_sum):
    max_subarrays = 0
    current_sum = 0
    subarray_length = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        subarray_length += 1

        if current_sum == target_sum and subarray_length >= 4:
            max_subarrays += 1
            current_sum = 0
            subarray_length = 0

        elif current_sum > target_sum:
            current_sum = arr[i]
            subarray_length = 1

    return max_subarrays