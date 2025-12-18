"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given positive integer `n` using recursion. The function should return an error message if `n` is a negative number, and it should handle large inputs efficiently in terms of time and space complexity.
"""

def factorial(n):
    if n < 0:
        return "Error: Input must be a positive integer."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)