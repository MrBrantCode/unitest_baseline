"""
QUESTION:
Create a recursive function named `factorial(n)` that calculates the factorial value of a specified integer `n`. The function should handle any integer input within the range of 1 to 50. Include exception handling to check if the input is within the defined range and is an integer, returning an error message if the check fails.
"""

def factorial(n):
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    elif n < 1 or n > 50:
        return "Error: Input must be within the range 1 to 50"
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)