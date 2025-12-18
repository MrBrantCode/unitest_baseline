"""
QUESTION:
Write a recursive function `calculate_factorial(n)` that calculates the factorial of a given number `n`. The function should return an error message if `n` is a negative number.
"""

def calculate_factorial(n):
    if n < 0:
        return "Error: factorial is undefined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)