"""
QUESTION:
Implement a function `count_ways_to_climb` that takes an integer `n` (1 <= n <= 45) representing the number of steps in a staircase and returns the total number of distinct ways to reach the top, where you can climb the staircase by either taking one step or two steps at a time.
"""

def count_ways_to_climb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        first = 1
        second = 2
        for _ in range(3, n + 1):
            current = first + second
            first = second
            second = current
        return second