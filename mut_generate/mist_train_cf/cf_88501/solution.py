"""
QUESTION:
Write a function named `calculate_area_and_perimeter` that takes one argument `side` representing the length of a side of a regular hexagon, and returns a tuple containing the area and perimeter of the hexagon. The area should be calculated using the formula A = (3 * sqrt(3) * side^2) / 2, and the perimeter should be calculated using the formula P = 6 * side. Use the `math` module for the square root calculation and correct exponentiation operator.
"""

import math

def calculate_area_and_perimeter(side):
    area = (3 * math.sqrt(3) * side**2) / 2
    perimeter = 6 * side
    return area, perimeter