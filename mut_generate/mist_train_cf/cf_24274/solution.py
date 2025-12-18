"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given positive integer. The function should take an integer `n` as input and return its factorial. The input integer `n` is assumed to be a non-negative integer.
"""

def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)