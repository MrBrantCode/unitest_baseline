"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number `n` using recursion, where `n` is a non-negative integer. The function should have a base case to prevent infinite recursion and should return the correct result for any valid input.
"""

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n-1)  # Recursive call