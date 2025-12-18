"""
QUESTION:
Implement a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number using dynamic programming. The Fibonacci sequence is defined as F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. The function should be able to handle inputs where n is 0 or greater.
"""

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]