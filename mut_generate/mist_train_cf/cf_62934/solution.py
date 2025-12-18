"""
QUESTION:
Given a positive integer `n`, implement the function `minOperations(n: int) -> int`. This function should return the minimum number of operations needed for `n` to become `1`. The allowed operations are: 
- If `n` is even, replace `n` with `n / 2`.
- If `n` is odd, replace `n` with either `n + 1`, `n - 1`, or `n * 2`.
The input `n` is constrained to `1 <= n <= 2^31 - 1`.
"""

def minOperations(n: int) -> int:
    dp = [0, 0, 1, 2] + [0] * (n - 3)
    for i in range(4, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1] + 1) + 1
        else:
            dp[i] = min(dp[i - 1], dp[(i + 1) // 2] + 1) + 1
    return dp[n]