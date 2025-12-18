"""
QUESTION:
Write a function named "calculate_area" that takes in six parameters: x1, y1, x2, y2, x3, y3, representing the coordinates of the three vertices of a triangle. The function should return the area of the triangle, rounded to the nearest integer. Assume that the given coordinates will always form a valid triangle.
"""

import math

def calculate_area(x1, y1, x2, y2, x3, y3):
    side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return round(area)