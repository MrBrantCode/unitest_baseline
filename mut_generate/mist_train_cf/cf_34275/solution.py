"""
QUESTION:
Implement a function `climbStairs` that takes a non-negative integer `n` as input, representing the total number of steps in a staircase, and returns the total number of unique ways to reach the top of the staircase by climbing either 1 or 2 steps at a time.
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