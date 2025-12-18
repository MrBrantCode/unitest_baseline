"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a positive integer `n` using recursion. The function should have a time complexity of O(n) and a space complexity of O(n). It should also handle edge cases, returning an error message if `n` is a negative integer.
"""

def factorial(n):
    # Check for invalid input
    if n < 0:
        return "Error: Input must be a positive integer."
    
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n - 1)