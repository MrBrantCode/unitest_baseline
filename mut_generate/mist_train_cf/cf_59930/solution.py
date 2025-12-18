"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given integer `n` using recursion, handling edge cases where `n` is 0 or a negative integer, and returns "Invalid input" if `n` is not an integer.
"""

def factorial(n):
    if not isinstance(n, int):    # Check if the input is not an integer
        return "Invalid input"
    elif n < 0:    # Check if the input is a negative integer
        return "Invalid input" # Changed this to "Invalid input"
    elif n == 0:    # Check if the input is 0
        return 1
    else:
        return n * factorial(n-1)   # Recursive call