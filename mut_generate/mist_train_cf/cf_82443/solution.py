"""
QUESTION:
Create a recursive function named `factorial` that calculates the factorial of a given integer `n`. The function should return 1 for `n` equal to 0 or 1 and the product of `n` and the factorial of `n-1` for larger `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
       return 1
    else:
       return n * factorial(n - 1)