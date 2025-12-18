"""
QUESTION:
Write a function named `factorial` that takes a string of digits as input, converts it to an integer, and returns the factorial of the integer. The function should work for any non-negative integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)