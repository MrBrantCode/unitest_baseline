"""
QUESTION:
Design a recursive function named `fibonacci` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should handle invalid inputs (non-positive integers) and return an error message.
"""

def fibonacci(n):
    if n <= 0:
        return "Error: Invalid input. Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)