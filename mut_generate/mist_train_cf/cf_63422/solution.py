"""
QUESTION:
Given two integers `n` and `k`, find how many different arrays consist of numbers from 1 to `n` such that there are exactly `k` inverse pairs and the array is in non-decreasing order. The answer should be modulo 10^9 + 7. Note: The integer `n` is in the range [1, 1000] and `k` is in the range [0, 1000]. Implement the function `kInversePairs(n, k)` to solve this problem.
"""

def kInversePairs(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
            if j - i >= 0:
                dp[i][j] -= dp[i - 1][j - i]
                dp[i][j] %= MOD
    return dp[n][k]