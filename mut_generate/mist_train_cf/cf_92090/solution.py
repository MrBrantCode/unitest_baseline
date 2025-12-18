"""
QUESTION:
Write a recursive function called `factorial` that calculates the factorial of a given integer `n`. The function should return an error message if `n` is a negative number and handle large inputs efficiently.
"""

def factorial(n):
    if n < 0:
        return "Error: Input must be a positive integer."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)