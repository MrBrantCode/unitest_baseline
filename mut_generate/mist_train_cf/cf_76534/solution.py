"""
QUESTION:
Create a function `foo(x, y, z, w=None)` that takes four parameters, all of which are expected to be numeric-long data type. Ensure that 'z' is always set to 0, 'w' is calculated as the absolute difference between 'x' and 'y', and include error handling to return an error message if 'x' or 'y' are not numeric values.
"""

def foo(x, y, z, w=None):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return "Error: both x and y must be numeric values"
    else:
        z = 0
        w = abs(x - y)
        return x, y, z, w