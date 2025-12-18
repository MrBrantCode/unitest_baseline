"""
QUESTION:
Create a function named `factorial(n)` that takes a non-negative integer `n` as input and returns its factorial. The function should use recursion (self-referencing) to calculate the factorial, which is the product of all positive integers less than or equal to `n`. The function should have a base case to handle the recursion termination.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)