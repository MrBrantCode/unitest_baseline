"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given number `n` using recursion. The function should return an error message if `n` is a negative number.
"""

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)