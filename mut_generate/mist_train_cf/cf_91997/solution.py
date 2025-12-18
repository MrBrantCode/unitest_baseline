"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should use recursion and include at least two base cases. Implement the function in Python.
"""

def factorial(n):
    # Base case 1: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive call: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n - 1)