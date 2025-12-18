"""
QUESTION:
Write a function named `pentagon_properties` that takes the side length of a regular pentagon as input and returns its perimeter and area. The function should also be used to calculate the perimeter and area of the pentagram formed by the pentagon's diagonals. Assume that the input side length is a positive value.
"""

import math

def pentagon_properties(side_length):
    perimeter = 5 * side_length
    apothem = side_length / (2 * math.tan(math.pi/5))
    area = 0.5 * perimeter * apothem
    triangle_base = side_length
    triangle_height = side_length / (2 * math.sin(math.pi/5))
    triangle_area = 0.5 * triangle_base * triangle_height
    pentagram_area = area + 5 * triangle_area
    return perimeter, area, perimeter, pentagram_area