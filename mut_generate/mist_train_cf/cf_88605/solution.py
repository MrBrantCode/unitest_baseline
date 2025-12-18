"""
QUESTION:
Implement a recursive function named `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should return an error message if `n` is not a positive integer (i.e., `n` is a float, negative, or a non-integer) or if `n` is greater than 10^6.
"""

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Error case: input is a float or negative integer
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a positive integer."

    # Error case: input is greater than 10^6
    if n > 10**6:
        return "Error: Input must be less than or equal to 10^6."

    # Recursive case: calculate factorial
    return n * factorial(n-1)