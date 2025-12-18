"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the first `n+1` elements in the Fibonacci sequence defined by the recurrence relation F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. The function should be optimized for both time complexity and space complexity and be able to handle inputs up to n = 1000.
"""

def fibonacci(n):
    fib = [0, 1]  # Initialize the sequence with the first two elements

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib