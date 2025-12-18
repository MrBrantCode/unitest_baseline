"""
QUESTION:
Write a function `fibonacci` to calculate the nth Fibonacci number in the series, where the Fibonacci series is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)