"""
QUESTION:
Implement the `climb_stairs` function that takes an integer `n` (1 ≤ n ≤ 45) as input, where `n` represents the number of steps in a staircase, and returns the total number of unique ways to climb the staircase, where you can climb either 1 or 2 steps at a time.
"""

def climb_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]