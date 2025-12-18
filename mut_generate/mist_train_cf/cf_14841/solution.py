"""
QUESTION:
Write a function named `fibonacci` that calculates and returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. In this case, the function should return the 50th number in the sequence.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b