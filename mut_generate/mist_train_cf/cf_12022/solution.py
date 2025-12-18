"""
QUESTION:
Write a Python function named `factorial(n)` that takes an integer `n` as input and returns its factorial. The function should handle invalid inputs, including non-integer and negative numbers, by returning an error message. The function should also handle the base case where `n` is 0.
"""

def factorial(n):
    # check if the input is a positive integer
    if not isinstance(n, int) or n < 0:
        return "Factorial is undefined for negative numbers and non-integers."
    
    # base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # recursive case: multiply n by factorial of (n-1)
    return n * factorial(n - 1)