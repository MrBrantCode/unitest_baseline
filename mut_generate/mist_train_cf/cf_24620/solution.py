"""
QUESTION:
Write a function `fibonacci` to calculate the nth term in the Fibonacci series. The Fibonacci series is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the nth term. The function should be able to handle inputs where `n` is 0 or 1.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)