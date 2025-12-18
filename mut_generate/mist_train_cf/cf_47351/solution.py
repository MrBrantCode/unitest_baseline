"""
QUESTION:
Write a Python function `fibonacci(n)` that calculates the nth number in the Fibonacci sequence using dynamic programming, where `n` is a non-negative integer. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]