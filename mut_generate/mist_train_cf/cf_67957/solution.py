"""
QUESTION:
Write a function `fib(n)` that returns the nth Fibonacci number using memoization, where the Fibonacci sequence is defined by the recurrence relation `F(n) = F(n-1) + F(n-2)` with base cases `F(0) = 0` and `F(1) = 1`. The function should store computed Fibonacci values in a dictionary to avoid redundant calculations.
"""

memo = {0: 0, 1: 1}  # Base cases

def entrance(n):
    if not n in memo:
        memo[n] = entrance(n-1) + entrance(n-2)  # Memoize computed Fibonacci value
    return memo[n]