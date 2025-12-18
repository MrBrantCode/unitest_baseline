"""
QUESTION:
Write a function `fibonacci(n)` that returns the nth Fibonacci number. The input `n` should be a positive integer. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. If `n` is not a positive integer, the function should return an error message.
"""

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b