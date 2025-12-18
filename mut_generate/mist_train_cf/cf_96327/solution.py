"""
QUESTION:
Write a function `calculate_rectangle_properties(points)` that calculates the area and perimeter of a rectangle given its four corner points in the Cartesian coordinate system. The corner points are represented as a list of lists `points`, where each inner list contains two integers representing the x and y coordinates of a point. The function should return a tuple containing the area and perimeter of the rectangle, and it should be able to handle rectangles that are not aligned with the x and y axes.
"""

import math

def calculate_rectangle_properties(points):
    side1 = math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)
    side2 = math.sqrt((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2)

    area = side1 * side2
    perimeter = 2 * (side1 + side2)

    return area, perimeter