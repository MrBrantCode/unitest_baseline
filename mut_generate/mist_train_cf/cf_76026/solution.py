"""
QUESTION:
Write a function `herons_formula` that takes three sides of an isosceles triangle as input (a, b, c), where a and b are the equal sides and c is the base. Use Heron's formula to calculate the area of the triangle and return the result. The function should work for any valid input values, assuming a and b are the asymmetrical sides and c is the base measurement.
"""

import math

def herons_formula(a, b, c):
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))