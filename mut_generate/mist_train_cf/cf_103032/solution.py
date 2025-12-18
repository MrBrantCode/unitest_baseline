"""
QUESTION:
Write a function `fibonacci(a, b, n)` to calculate the nth number in a Fibonacci-like sequence that starts with `a` and `b`, where `n` is a non-negative integer and `a` and `b` are the first two numbers in the sequence. The function should use recursion to calculate the result.
"""

def fibonacci(a, b, n):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(a, b, n-1) + fibonacci(a, b, n-2)