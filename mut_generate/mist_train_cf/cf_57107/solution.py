"""
QUESTION:
Write a Python function named `factorial` that uses recursion to calculate the factorial of a given integer. The function should only accept non-negative integers as input and should return the correct factorial result.
"""

def factorial(n):
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)