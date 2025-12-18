"""
QUESTION:
Write a function named 'fact' that takes an integer 'n' as input and returns its factorial. The function should follow these rules: the factorial of 0 is 1, and the factorial of any other number 'n' is 'n' multiplied by the factorial of 'n-1'.
"""

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)