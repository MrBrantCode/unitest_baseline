"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given number `n` using recursion. The function should take an integer `n` as input and return the factorial of `n`. The function should handle the base case where `n` equals 0.
"""

def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)