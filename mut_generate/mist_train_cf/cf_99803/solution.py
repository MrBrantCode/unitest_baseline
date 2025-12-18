"""
QUESTION:
Write a function named `factorial` that takes a positive integer `n` and returns the factorial of `n` using recursion without exceeding a maximum recursion depth of 1000. The function should also include error handling to return informative error messages for non-integer input values and values less than 0 or greater than 1000.
"""

def factorial(n):
    if not isinstance(n, int):
        return "Error: Input value must be an integer."
    elif n < 0:
        return "Error: Input value must be negative."
    elif n > 1000:
        return "Error: Input value must be less than or equal to 1000."
    elif n == 0:
        return 1
    else:
        try:
            return n * factorial(n-1)
        except RecursionError:
            return "Error: Maximum recursion depth exceeded."