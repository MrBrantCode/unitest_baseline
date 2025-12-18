"""
QUESTION:
You are given a positive integer `n`, representing the total number of steps in a staircase. You can climb either 1 or 2 steps at a time. Write a function `climbStairs` that takes `n` (1 <= n <= 45) as input and returns the total number of unique ways to reach the top of the staircase.
"""

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        first = 1
        second = 2
        for i in range(3, n+1):
            current = first + second
            first = second
            second = current
        return second