"""
QUESTION:
Write a function `max_subarray_sum(arr)` that takes an integer array `arr` as input and returns the largest sum of all possible subarray sums, where the subarray must have a length of at least 2, be contiguous, and not include adjacent elements. If the length of `arr` is less than 3, the function should return 0.
"""

def max_subarray_sum(arr):
    n = len(arr)
    if n < 3:
        return 0

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]