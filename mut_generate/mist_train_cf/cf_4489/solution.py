"""
QUESTION:
Create a function `calculate_area_and_perimeter` that calculates the area and perimeter of a regular hexagon given the length of one side. The area must be calculated using the formula A = (3 * sqrt(3) * side^2) / 2 and the perimeter must be calculated using the formula P = 6 * side. The function should return the calculated area and perimeter.
"""

import math

def calculate_area_and_perimeter(side):
    area = (3 * math.sqrt(3) * side**2) / 2
    perimeter = 6 * side
    return area, perimeter