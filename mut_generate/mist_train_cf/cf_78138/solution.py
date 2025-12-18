"""
QUESTION:
Write a function `integerReplacement(n)` that takes a positive integer `n` as input and returns the minimum number of operations needed to transform `n` into 1. The allowed operations are:
- If `n` is even, `n` can be replaced with `n / 2`.
- If `n` is odd, `n` can be replaced with `n + 1`, `n - 1`, or `n * 2`, but the operation that moves closer to 1 is preferred.

Constraints: `1 <= n <= 2^31 - 1`
"""

def integerReplacement(n):
    dp = [0] * (n+2)
    for x in range(2, n+1):
        if x % 2 == 0:
            dp[x] = dp[x//2] + 1
        else:
            dp[x] = min(dp[x - 1], dp[(x + 1)//2] + 1) + 1
    return dp[n]