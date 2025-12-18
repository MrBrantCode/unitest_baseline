"""
QUESTION:
Create a function called `multiply` that takes two parameters, `x` and `y`. The function should return the product of `x` and `y` if both are numbers (either integers or floats). If either `x` or `y` is not a number, the function should return 'Not a number'.
"""

def multiply(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return 'Not a number'
    else:
        return x * y