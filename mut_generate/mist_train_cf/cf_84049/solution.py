"""
QUESTION:
Implement a function named `fib(n)` that calculates the nth Fibonacci number, where the Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. The function should be optimized to have a time complexity better than exponential O(2^n), using strategies such as dynamic programming or memoization. The input `n` will be a non-negative integer.
"""

def fib(n, memo = {}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]