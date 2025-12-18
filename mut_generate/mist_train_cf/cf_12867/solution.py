"""
QUESTION:
Write a function named `factorial_recursive` that calculates the factorial of a given integer `n` using recursion. The function should return the factorial of `n`. The function must use recursion instead of a loop and should have a base case to handle the recursion.
"""

def factorial_recursive(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: call the function itself with n-1 and multiply it with n
    else:
        return n * factorial_recursive(n-1)