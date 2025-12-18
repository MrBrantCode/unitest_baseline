"""
QUESTION:
Write a function named `fibonacci` to calculate the nth Fibonacci number, where each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should be recursive and handle cases where `n` is 0 or 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)