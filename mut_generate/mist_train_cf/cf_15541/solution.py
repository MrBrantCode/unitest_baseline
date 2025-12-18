"""
QUESTION:
Create a function `closest_decimal_approximation(n, precision)` that finds the closest decimal approximation of a given number `n` using a recursive algorithm, with a maximum precision of `precision` decimal places.
"""

def closest_decimal_approximation(n, precision):
    # Base case: if the desired precision is reached, return the current approximation
    if precision == 0:
        return n

    # Recursive case: add decimal places by multiplying n by 10
    return closest_decimal_approximation(n * 10, precision - 1)