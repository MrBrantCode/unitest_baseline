"""
QUESTION:
Given an array of integers, implement a function `maxNonContiguousSubsequenceSum(arr)` that calculates the maximum sum of a non-contiguous subsequence within the array. The function should use dynamic programming and return the maximum sum. The input array can contain both positive and negative numbers.
"""

def maxNonContiguousSubsequenceSum(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    # dp[i] will store the maximum sum of non-contiguous subsequence till index i.
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])

    for i in range(2, n):
        # for each element we have two choices, 
        # either we include in our subsequence or we don’t include it.
        dp[i] = max(arr[i], max(dp[i-1], dp[i-2]+arr[i]))

    return dp[n-1]