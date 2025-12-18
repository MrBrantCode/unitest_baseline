"""
QUESTION:
Write a function called `FibFib(n)` that calculates the nth number in a sequence where each subsequent number is the sum of the previous three numbers, starting with 0, 0, 1. The function should use memoization to store already calculated values and return an error for negative input values.
"""

def FibFib(n, memo = {0: 0, 1: 0, 2: 1}):
    if n < 0:
        return "Invalid input: n must be a non-negative integer"
    if n not in memo:
        memo[n] = FibFib(n-1, memo) + FibFib(n-2, memo) + FibFib(n-3, memo)
    return memo[n]