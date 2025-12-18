"""
QUESTION:
Write a function `subsetsum` that takes a list of numbers `arr` and a target sum `target`, and returns a boolean indicating whether a subset of `arr` sums up to `target`. The function should return True if such a subset exists, and False otherwise. The input list `arr` and target `target` are non-negative integers, and the function should be efficient for large inputs.
"""

def subsetsum(arr, target):
    n = len(arr)
    dp = [[False for x in range(target + 1)] for y in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(target + 1):
            dp[i][j] = dp[i-1][j] or (arr[i-1] <= j and dp[i-1][j - arr[i-1]])
    return dp[n][target]