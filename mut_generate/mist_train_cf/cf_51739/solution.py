"""
QUESTION:
Write a Python function `is_integer_product` that takes three string representations of fractions as input in the format `<numerator>/<denominator>`, where both the numerator and denominator are integers greater than zero. The function should simplify the algebraic expression `x * n * y` and return `True` if the result is an integer, `False` otherwise.
"""

def is_integer_product(x, n, y):
    # Split the strings to separate the numerator and denominator
    xNum, xDen = map(int, x.split('/'))
    nNum, nDen = map(int, n.split('/'))
    yNum, yDen = map(int, y.split('/'))

    # Calculate the result
    result = (xNum * nNum * yNum) / (xDen * nDen * yDen)

    # Return true if the result is an integer, false otherwise
    return result.is_integer()