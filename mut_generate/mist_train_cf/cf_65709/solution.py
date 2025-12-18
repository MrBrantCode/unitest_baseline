"""
QUESTION:
Create a function named `calculate_ellipse_area` that takes two arguments, the semi-major axis `a` and the semi-minor axis `b`, and returns the area of an ellipse. Both `a` and `b` should be non-negative; if either is negative, the function should raise an exception.
"""

import math

class InvalidEllipseArguments(Exception): pass

def calculate_ellipse_area(a, b):
    if a < 0 or b < 0:
        raise InvalidEllipseArguments("Both semi-major and semi-minor axes should be non-negative")

    return math.pi * a * b