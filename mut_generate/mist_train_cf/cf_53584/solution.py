"""
QUESTION:
Calculate the surface area of an isosceles triangle using the semi-perimeter estimation technique. Implement a function named `calculate_surface_area` that takes three arguments: `side1`, `side2`, and `base`, representing the lengths of the two equal sides and the base of the triangle, respectively. The function should return the calculated surface area. The input values for `side1`, `side2`, and `base` are 7, 7, and 8 units, respectively.
"""

import math

def calculate_surface_area(side1, side2, base):
    # calculate semi-perimeter
    s = (side1 + side2 + base) / 2
    
    # calculate the surface area
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - base))
    
    return area