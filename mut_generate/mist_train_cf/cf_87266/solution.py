"""
QUESTION:
Implement a function called `factorial` that calculates the factorial of a given non-negative integer without using any built-in functions or libraries. The function should return the product of all positive integers less than or equal to the input number.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)