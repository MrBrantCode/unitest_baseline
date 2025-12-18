"""
QUESTION:
Write a function named `max_subarray_sum` that takes an integer array as input and returns the largest sum of all possible subarray sums. The subarray must have a length of at least 2 and cannot include adjacent elements.
"""

def max_subarray_sum(arr):
    if len(arr) < 2:
        return 0

    dp = [0] * len(arr)
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])

    return dp[-1]