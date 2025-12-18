"""
QUESTION:
Implement a function named `factorial(n)` to calculate the factorial of a given number `n`. The function should use recursion and handle the following conditions: `n` must be an integer, `n` must be a non-negative number, and `n` must be less than 1000 due to Python's recursion limit. If any of these conditions are not met, the function should raise an error message with the corresponding reason.
"""

def factorial(n):
    assert isinstance(n, int), "Error: input must be an integer."
    assert n >= 0, "Error: input must be positive."
    assert n < 1000, "Error: input must be less than 1000 because of recursion limit."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)