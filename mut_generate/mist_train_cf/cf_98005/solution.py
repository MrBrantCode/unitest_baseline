"""
QUESTION:
Create a function named `ellipse_circumference` that takes two parameters, `a` and `b`, which are the lengths of the major and minor axes of an ellipse, respectively. The function should return an approximation of the circumference of the ellipse. Use the approximation formula `C = pi * (a + b) * (1 + 3 * ((a - b) / (a + b))**2) / (10 + (4 - 3 * ((a - b) / (a + b))**2)**0.5)`.
"""

import math

def ellipse_circumference(a, b):
    h = ((a - b) / (a + b))**2
    return math.pi * (a + b) * (1 + 3 * h / (10 + (4 - 3 * h)**0.5))