"""
QUESTION:
You are given a staircase with n steps and can climb the staircase by taking either 1 step, 2 steps, or 3 steps at a time. Write a function `countWays` that takes an integer `n` as input and returns the number of distinct ways to reach the top of the staircase.
"""

def countWays(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]