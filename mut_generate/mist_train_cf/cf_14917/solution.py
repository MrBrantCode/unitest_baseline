"""
QUESTION:
Design a recursive algorithm with two functions, `fibonacci(n)` and `fibonacciSum(n)`. The `fibonacci(n)` function should return the nth Fibonacci number. The `fibonacciSum(n)` function should return the sum of all Fibonacci numbers up to the nth index. The Fibonacci sequence starts with 0 and 1. Implement these functions in Python.
"""

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacciSum(n):
    """Return the sum of all Fibonacci numbers up to the nth index."""
    if n == 0:
        return 0
    else:
        return fibonacci(n) + fibonacciSum(n-1)