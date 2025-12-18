"""
QUESTION:
Create a function `sum_of_squares(n)` that calculates the sum of squares of the first n natural numbers. The function should handle negative values for n and ensure the result is within the range of a 64-bit signed integer. Do not use the `math` library or built-in functions that directly solve the problem.
"""

def sum_of_squares(n):
    if n < 0:
        return "Invalid input"

    result = n * (n + 1) * (2 * n + 1) // 6

    return result