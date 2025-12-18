"""
QUESTION:
Write a function `calculate_rectangle_properties` in Python that calculates the area and perimeter of a rectangle given its four corner points in the Cartesian coordinate system, where the corner points are given in the format [x, y] and the rectangle is not necessarily aligned with the x and y axes. The function should take a list of four corner points as input and return the area and perimeter of the rectangle as output.
"""

import math

def calculate_rectangle_properties(points):
    # Calculate the lengths of the sides
    side1 = math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)
    side2 = math.sqrt((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2)

    # Calculate the area and perimeter
    area = side1 * side2
    perimeter = 2 * (side1 + side2)

    return area, perimeter