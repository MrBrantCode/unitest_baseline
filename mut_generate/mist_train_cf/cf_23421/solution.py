"""
QUESTION:
Create a function called `fibonacci(n)` that takes an integer `n` as an argument and returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should handle cases where `n` is less than 0, 0, or 1, and return the corresponding Fibonacci number.
"""

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)