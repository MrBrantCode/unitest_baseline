"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer using recursion. The function should take one integer parameter `n` and return its factorial. Implement this function in a separate module.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)