"""
QUESTION:
Write a function `recursive_sum(n)` that calculates the sum of all integers from 0 to `n` using recursion. The function should take one integer parameter `n` and return the calculated sum.
"""

def entrance(n):
    if n == 0:
        return 0
    else:
        return n + entrance(n-1)