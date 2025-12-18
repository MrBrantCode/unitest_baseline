"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a positive integer `n` where 1 ≤ n ≤ 20.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)