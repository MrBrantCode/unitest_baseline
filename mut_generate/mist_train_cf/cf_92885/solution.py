"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given positive integer `n` using recursion, where `n` is restricted to be less than or equal to 10. The function should return the calculated factorial.
"""

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: call the function with n-1 and multiply it with n
    else:
        return n * factorial(n - 1)