"""
QUESTION:
Implement a recursive function `factorial_recursive(n)` to calculate the factorial of a given integer `n`. The function should use recursion instead of a loop and return the factorial of `n`.
"""

def factorial_recursive(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: call the function itself with n-1 and multiply it with n
    else:
        return n * factorial_recursive(n-1)