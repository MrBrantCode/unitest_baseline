"""
QUESTION:
Write a function named `fibonacci(n)` that generates and returns the Fibonacci sequence up to the n-th number using recursion and memoization to optimize for large values of n. The function should handle non-negative integers for n.
"""

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
    return computed[n]