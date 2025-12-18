"""
QUESTION:
Implement a function `countWaysToReachTop` that calculates the total number of distinct ways to reach the top of a staircase with `n` steps, where `n` is an integer between 1 and 45 inclusive, and you can climb either 1 or 2 steps at a time.
"""

def countWaysToReachTop(n):
    if n <= 1:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b