"""
QUESTION:
Implement a function `nth_fib(n)` that calculates the nth Fibonacci number, where each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the nth Fibonacci number, or None for non-positive input values.
"""

def nth_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b