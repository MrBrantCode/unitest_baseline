"""
QUESTION:
Implement a recursive function named `factorial` in Python that calculates the factorial of a positive integer. The function should take a single integer `n` as input and return its factorial as output. The function should not use any built-in functions or libraries.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)