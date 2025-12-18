"""
QUESTION:
Write a recursive function named `fibonacci` that takes an integer `n` as input and returns the `n`-th Fibonacci number, where `F(n) = F(n-1) + F(n-2)` with base cases `F(0) = 0` and `F(1) = 1`.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)