"""
QUESTION:
Write a function `longest_sum_zero` that takes an array of integers as input and returns the length of the longest subarray with a sum of 0.
"""

def longest_sum_zero(arr):
    left = 0
    max_len = 0
    total_sum = 0
    hash_map = dict()
    for right in range(len(arr)):
        total_sum += arr[right]
        if total_sum == 0:
            max_len = max(max_len, right - left + 1)
        if total_sum in hash_map:
            left = max(left, hash_map[total_sum] + 1)
            max_len = max(max_len, right - left + 1)
        hash_map[total_sum] = right

    return max_len