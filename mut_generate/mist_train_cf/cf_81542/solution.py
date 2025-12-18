"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer input using recursion. The function should return a meaningful error message for anomalous inputs, including negative integers and non-integers.
"""

def factorial(n):
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    if n < 0:
        return "Error: Input must be a non-negative integer"
      
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)