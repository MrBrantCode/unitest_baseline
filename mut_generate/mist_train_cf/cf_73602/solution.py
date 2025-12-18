"""
QUESTION:
Write a function `fib(n)` that calculates the nth Fibonacci number, with a time complexity better than O(2^n), to efficiently handle large inputs like 10^6.
"""

def fib(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]