"""
QUESTION:
Write a recursive function named `factorial` that calculates the factorial of a given non-negative integer without using any arithmetic operators (+, -, *, /). The function should return `None` for negative inputs.
"""

def factorial(n):
    def multiply(a, b):
        if b == 0:
            return 0
        else:
            return a + multiply(a, b - 1)

    if n < 0:
        return None  
    elif n == 0:
        return 1
    else:
        return multiply(n, factorial(n - 1))