"""
QUESTION:
Write a recursive function `max_subarray(arr, n, k)` that calculates the maximum cumulative total attached with a contiguous subarray of pre-defined size 'k' within a numerical array of length 'n'. The function should handle edge cases where the value of 'k' is greater than 'n' or less than 1.
"""

def max_subarray(arr, n, k):
    # if k is less than 1 or greater than n, return 0
    if k < 1 or k > n:
        return 0
    #initialize maximum sum and current sum
    max_sum = float("-inf")
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]
    # helper function to calculate maximum subarray sum
    def calc_sum(i, current_sum):
        nonlocal max_sum
        if i >= n:
            return current_sum
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
        return calc_sum(i + 1, current_sum)
    calc_sum(k, current_sum)
    return max_sum