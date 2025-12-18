"""
QUESTION:
You are given a staircase with n steps. Write a function `climb_stairs` that takes an integer `n` as input and returns the distinct number of ways to reach the top of the staircase, given that you can climb either 1 or 2 steps at a time. The function should use dynamic programming to efficiently calculate the result.
"""

def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]