"""
QUESTION:
You are given a staircase with `n` steps. You can climb the staircase by taking either 1 or 2 steps at a time. Implement the `count_ways_to_climb_stairs(n)` function to calculate the total number of distinct ways to reach the top of the staircase. The function should take an integer `n` as input and return the total number of distinct ways to reach the top.
"""

def count_ways_to_climb_stairs(n):
    if n <= 1:
        return 1
    else:
        # Initialize the number of ways to climb the stairs with 1 step or 2 steps
        ways = [1, 2]
        for i in range(2, n):
            # Calculate the total ways to reach the current step by adding the ways to reach the previous two steps
            ways.append(ways[i - 1] + ways[i - 2])
        return ways[n - 1]