"""
QUESTION:
Construct a function `binomial_cumulative_product(n)` that calculates the cumulative product of consecutive binomial coefficients within a given range `n`. The function should handle edge cases where `n` is a negative number, a non-integer, a floating point number that is not a whole number, or a complex number. If the input is invalid, the function should return a meaningful error message.
"""

import math

def binomial_cumulative_product(n):
    # Error handling
    if not isinstance(n, (int, float)):
        return 'Error: input must be a positive integer or a floating point number.'
    elif isinstance(n, float) and not n.is_integer():
        return 'Error: floating point numbers must be whole numbers.'
    elif n < 0:
        return 'Error: input must be a positive number.'
    
    # Convert to integer if the input is a floating point
    if isinstance(n, float):
        n = int(n)

    # Calculate cumulative product
    product = 1
    for i in range(n):
        try:
            product *= math.comb(n, i)
        except OverflowError:
            return 'Error: result is too large.'

    return product