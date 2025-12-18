"""
QUESTION:
Write a function `rod_cutting(arr, n)` that uses dynamic programming to find the maximum value that can be obtained by cutting a rod of length `n` into smaller pieces, where `arr[i]` represents the value of a piece of length `i+1`. The function should take an array `arr` and an integer `n` as input, and return the maximum value that can be obtained. The length of the rod is not more than the length of the array `arr`.
"""

def unbound_knapsack(arr, n):
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(i):
            dp[i] = max(dp[i], arr[j] + dp[i - j - 1])
    return dp[n]