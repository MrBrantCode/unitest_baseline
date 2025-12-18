"""
QUESTION:
Write a function `countWaysToReachTop` that takes an integer `n` as input, representing the total number of steps in a staircase, and returns the total number of distinct ways to reach the top, where you can climb the staircase by either taking one step or two steps at a time. The function should be efficient and able to handle large inputs.
"""

def countWaysToReachTop(n):
    if n <= 1:
        return n
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b if n != 2 else 2