"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a non-negative integer `n` using recursion. The function should have a time complexity of O(n) and handle cases where the input is negative or a floating-point number by returning an error message.
"""

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer."
    if n == 0:
        return 1
    return n * factorial(n-1)