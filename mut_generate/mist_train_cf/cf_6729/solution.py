"""
QUESTION:
Write a function `f(n)` that calculates the sum of all numbers from 1 to `n` using recursion. The function should return 0 when `n` is 0.
"""

def f(n):
    if n == 0:
        return 0
    else:
        return n + f(n-1)