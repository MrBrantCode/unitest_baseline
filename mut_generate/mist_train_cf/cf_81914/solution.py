"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer `n`. The function should return an error message if `n` is less than 0, and return 1 if `n` is 0. The function should recursively calculate the factorial for positive integers.
"""

# function to calculate factorial
def factorial(n):
    if n < 0:
        return "Error! Factorial of a negative number does not exist."
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)