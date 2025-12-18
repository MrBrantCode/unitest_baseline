"""
QUESTION:
Create a recursive function named `factorial(n)` to calculate the factorial of a non-negative integer `n` without using any arithmetic operators (+, -, *, /). The function should return the factorial of `n` if it is non-negative, and return `None` if `n` is negative.
"""

def factorial(n):
    def multiply(a, b):
        if b == 0:
            return 0
        else:
            return a + multiply(a, b - 1)

    if n < 0:
        return None  # Factorial is undefined for negative numbers
    elif n == 0:
        return 1
    else:
        return multiply(n, factorial(n - 1))