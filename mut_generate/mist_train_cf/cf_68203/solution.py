"""
QUESTION:
Write a function `factorial_recursive` that calculates the factorial of a given integer `n` using recursion. The function should have a base case to stop the recursion and should call itself to solve the problem.
"""

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)