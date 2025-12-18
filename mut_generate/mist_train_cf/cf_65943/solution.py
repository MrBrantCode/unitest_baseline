"""
QUESTION:
Create a function called factorial(n) that calculates the factorial of a given integer n. The function should return an error message if n is a negative integer. Assume the input is an integer.
"""

def factorial(n):
    if n < 0:
        return "Error: Negative Input"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)