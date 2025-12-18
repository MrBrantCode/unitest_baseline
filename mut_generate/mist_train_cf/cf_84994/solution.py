"""
QUESTION:
Create a function named `fibonacci(n)` that returns the nth number in the Fibonacci series, where `n` is a non-negative integer. The Fibonacci series is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c