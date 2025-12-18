"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using dynamic programming. The Fibonacci sequence is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. The function should efficiently compute the nth Fibonacci number for large values of n.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]