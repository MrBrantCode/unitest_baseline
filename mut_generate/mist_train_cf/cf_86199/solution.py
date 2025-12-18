"""
QUESTION:
Implement a function called 'power' that takes two parameters, x and y, where x is a numeric value between 1 and 10 (inclusive) and y is an integer between 0 and 5 (inclusive). The function should calculate the result of 'x to the power of y' using a custom algorithm, handling any potential errors or edge cases, and return the result in scientific notation if it exceeds a dynamically determined threshold.
"""

import math

def power(x, y):
    # Check for invalid inputs
    if not isinstance(x, (int, float)) or not isinstance(y, int):
        return "Error: Invalid input. Please enter numeric values for x and y."

    # Check if x is between 1 and 10
    if not 1 <= x <= 10:
        return "Error: x should be between 1 and 10."

    # Check if y is between 0 and 5
    if not 0 <= y <= 5:
        return "Error: y should be between 0 and 5."

    # Custom algorithm for calculating power
    result = x ** y

    # Check if result exceeds threshold for scientific notation
    if result > 1e6:
        return "{:.2e}".format(result)
    else:
        return result