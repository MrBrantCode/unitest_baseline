"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The Fibonacci sequence is defined where a number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)