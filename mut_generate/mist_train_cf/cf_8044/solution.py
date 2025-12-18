"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a non-negative integer `n` using recursion. The function should have a time complexity of O(n) and handle input errors by returning an error message if `n` is negative.
"""

def factorial(n):
    # Input error handling
    if n < 0:
        return "Input must be a non-negative integer."
    # Base case
    if n == 0:
        return 1
    # Recursive call
    return n * factorial(n - 1)