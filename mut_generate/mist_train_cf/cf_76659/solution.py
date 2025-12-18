"""
QUESTION:
Write a Python function named `factorial(n)` that calculates the factorial of a given number `n` using recursion. The function should have a base case that returns 1 when `n` equals 1, and a recursive case that calls itself to calculate the factorial of `n-1`. The function should work for any positive integer `n` and return the correct factorial value.
"""

def factorial(n):
    if n == 1:
        return 1 
    else:
        return n * factorial(n-1) 