"""
QUESTION:
Write a function `calculate_area_perimeter(rectangle)` that calculates the area and perimeter of a rectangle given its four corner points in the Cartesian coordinate system. The corner points should be represented as a list of four lists, where each inner list contains two numbers representing the x and y coordinates of a point. The function should be able to handle rectangles that are not aligned with the x and y axes and are rotated at an angle other than 0 degrees with respect to the x and y axes.
"""

import math

def calculate_area_perimeter(rectangle):
    # Get the x and y coordinates of the four corner points
    x1, y1 = rectangle[0]
    x2, y2 = rectangle[1]
    x3, y3 = rectangle[2]
    x4, y4 = rectangle[3]

    # Calculate the distances between the corner points
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    width = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

    # Calculate the area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter