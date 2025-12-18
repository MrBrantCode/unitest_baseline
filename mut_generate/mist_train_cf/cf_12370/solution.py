"""
QUESTION:
Write a function named `rod_cutting` that takes an array of integers `arr` and an integer `n` as input, and returns the maximum value that can be obtained by cutting a rod of length `n`. The function should use dynamic programming with a time complexity of O(n^2) and a space complexity of O(n).
"""

def rod_cutting(arr, n):
    if n <= 0:
        return 0
    dp = [0] * (n+1)
    for i in range(1, n+1):
        max_val = 0
        for j in range(i):
            max_val = max(max_val, arr[j] + dp[i-j-1])
        dp[i] = max_val
    return dp[n]