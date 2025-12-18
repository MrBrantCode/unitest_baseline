"""
QUESTION:
Create a function called `identify_output(x)` that takes one argument `x`. The function should return -1 if `x` is a negative integer, 0 if `x` is 0, 1 if `x` is a positive integer, the integer value of `x` if `x` is a float or a string representation of an integer, and "Invalid input" if `x` is a non-numeric string or a non-integer/float/string type.
"""

def identify_output(x):
    if isinstance(x, int):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        elif x > 0:
            return 1
    elif isinstance(x, float):
        return int(x)
    elif isinstance(x, str):
        try:
            return int(x)
        except ValueError:
            return "Invalid input"
    else:
        return "Invalid input"