"""
QUESTION:
Create a recursive function named `factorial` to calculate the factorial of a given positive integer `n`. The function should work for `n` values less than or equal to a certain number. The function should return the product of all positive integers up to `n` and handle the base case where `n` equals 0.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)