"""
QUESTION:
Write a function `S(N)` that calculates the sum of the least number of jumps a flea needs to make to arrive at the interior of each upward-pointing triangle in the upper half of a regular hexagonal table with a side length of `N`. The function should take an integer `N` as input and return the calculated sum. The solution should be efficient and not require simulating the flea's jumps.
"""

def S(N):
    return 23 * ((3 * N**2 - 3 * N) // 2)