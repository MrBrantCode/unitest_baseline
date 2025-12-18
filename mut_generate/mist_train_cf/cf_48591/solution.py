"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using recursion and memoization, where `n` is a non-negative integer and the Fibonacci sequence is defined as: `fibonacci(0) = 0`, `fibonacci(1) = 1`, and `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` for `n > 1`. The function should use memoization to store previously computed Fibonacci numbers to avoid redundant calculations and achieve linear time complexity.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]