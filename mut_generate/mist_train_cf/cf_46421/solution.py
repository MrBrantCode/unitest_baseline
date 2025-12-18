"""
QUESTION:
Create a function `modified_foo` that takes one input `x` and returns three values: the square of `x`, the cube of `x`, and the square root of the absolute value of `x`. The function should handle exceptions for invalid inputs, including non-numeric inputs and inputs of the wrong type. If an exception occurs, the function should return a corresponding error message.
"""

def modified_foo(x):
    try:
        x = float(x)
        square = x**2
        cube = x**3
        sqrt_abs = abs(x)**0.5
        return square, cube, sqrt_abs
    except ValueError:
        return "Error: Invalid Input"
    except TypeError:
        return "Error: Wrong Type for Input"