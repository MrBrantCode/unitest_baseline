"""
QUESTION:
Implement a function `fib(n, memo={})` that calculates the nth Fibonacci number using recursion and memoization. The function should handle non-negative integers, including 0, and return an error message for negative integers.
"""

def fib(n, memo={}):
    if n < 0:
        return "Error: Input should be a non-negative integer"
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]