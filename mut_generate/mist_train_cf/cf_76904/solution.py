"""
QUESTION:
Write a function `fibonacci(n)` that calculates the `n-th` Fibonacci number using an iterative algorithm. The function should return the `n-th` Fibonacci number. The Fibonacci sequence is defined as `fib(0) = 0`, `fib(1) = 1`, and `fib(n) = fib(n-1) + fib(n-2)` for `n > 1`. The function should run in O(n) time or better and use O(1) space or better.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b