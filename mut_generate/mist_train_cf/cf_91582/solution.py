"""
QUESTION:
Write a recursive function named `fibonacci` that takes three parameters: `a`, `b`, and `n`. The function should return the nth number in a Fibonacci-like sequence where the first two numbers are `a` and `b`. The function should work for any non-negative integer `n`.
"""

def fibonacci(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(a, b, n-1) + fibonacci(a, b, n-2)