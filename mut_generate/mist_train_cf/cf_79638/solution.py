"""
QUESTION:
Write a function named `surface_area_of_prism` to calculate the surface area of a right-angled triangular prism. The function should take three parameters: the lengths of the two sides of the right-angled triangle (`a` and `b`) and the height of the prism (`h`). The function should return the total surface area of the prism, calculated using the lengths of the sides and height, and the Pythagorean theorem to find the length of the hypotenuse. The function should be implemented in a way that the returned surface area is in the square of the unit used for the input parameters.
"""

import math

def surface_area_of_prism(a, b, h):
    c = math.sqrt(a**2 + b**2)  # Calculating the length of the hypotenuse
    SA = a * b + a * h + b * h + h * c  # Calculating the surface area
    return SA