"""
QUESTION:
Implement a function `countWays` that calculates the total number of ways to reach the top of a staircase with `n` steps, where you can climb either 1 step, 2 steps, or 3 steps at a time. The function should take an integer `n` as input and return the total number of distinct ways to reach the top.
"""

def countWays(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        ways = [0] * (n + 1)
        ways[0], ways[1], ways[2] = 1, 1, 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
        return ways[n]