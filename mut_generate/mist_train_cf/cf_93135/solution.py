"""
QUESTION:
Implement a function `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should be recursive and not use any loops or temporary variables. The Fibonacci sequence is defined as `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` with base cases `fibonacci(0) = 0` and `fibonacci(1) = 1`.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)