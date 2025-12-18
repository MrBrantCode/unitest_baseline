"""
QUESTION:
You are tasked with implementing a function `climbStairs` that takes an integer `n` representing the total number of steps in a staircase, where you can climb either 1 or 2 steps at a time, and returns the total number of distinct ways to reach the top.
"""

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        first = 1
        second = 2
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second