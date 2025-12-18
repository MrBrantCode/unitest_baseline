"""
QUESTION:
Implement a recursive function named `fibonacci` that calculates the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)