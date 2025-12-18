"""
QUESTION:
Implement a function `countWays` that calculates the total number of unique ways to climb a staircase with `n` steps, where you can climb either 1 or 2 steps at a time, using dynamic programming. The function should take an integer `n` as input and return the total number of unique ways to climb the staircase.
"""

def countWays(n: int) -> int:
    if n <= 1:
        return 1
    # Create an array to store the number of ways to reach each step
    ways = [0] * (n + 1)
    ways[0], ways[1] = 1, 1  # Base cases for 0 and 1 step
    for i in range(2, n + 1):
        # The number of ways to reach step i is the sum of ways to reach step i-1 and step i-2
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]