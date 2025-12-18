"""
QUESTION:
Calculate the area and perimeter of a rectangle given its four corner points in the Cartesian coordinate system, where the corner points are represented as [x, y] and may not be aligned with the x and y axes. The function should be able to handle rectangles rotated at an angle other than 0 degrees. Implement the `calculate_area_perimeter(rectangle)` function to return the area and perimeter, where `rectangle` is a list of four [x, y] points. Assume the input rectangle is convex, non-degenerate, and has a non-zero area.
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