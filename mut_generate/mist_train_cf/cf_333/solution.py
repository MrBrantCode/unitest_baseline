"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given integer `n` using recursion, where `n` is between 1 and 20, inclusive. The time complexity of the solution should be less than or equal to O(n).
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)