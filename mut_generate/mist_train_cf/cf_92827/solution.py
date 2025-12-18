"""
QUESTION:
Create a recursive function named `factorial` that takes an integer `n` as input and returns its factorial. The function should handle the base case where `n` is 0.
"""

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n-1)