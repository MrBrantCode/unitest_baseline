"""
QUESTION:
Create a Python function named `factorial` that calculates the factorial of a given non-negative integer using recursion. The function should return an error message if the input is not a non-negative integer.
"""

def factorial(n):
    # check if the number is negative or decimal
    if not isinstance(n, int) or n < 0:
        return "Input should be non-negative integer"
    # base case: factorial of 0 is 1
    elif n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)