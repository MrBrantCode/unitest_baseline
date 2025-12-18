"""
QUESTION:
Write a function named `ellipse_circumference` that calculates the circumference of an ellipse given the lengths of its major and minor axes, `a` and `b` respectively, using the formula `C = pi * (a + b) * (1 + 3 * ((a - b) / (a + b))**2) / (10 + (4 - 3 * ((a - b) / (a + b))**2)**0.5)`. The function should take two parameters, `a` and `b`, which are the lengths of the major and minor axes respectively. The function should return the calculated circumference.
"""

import math

def ellipse_circumference(a, b):
    h = ((a - b) / (a + b))**2
    return math.pi * (a + b) * (1 + 3 * h / (10 + (4 - 3 * h)**0.5))