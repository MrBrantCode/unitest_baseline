"""
QUESTION:
Write a function named "calculate_area" that takes three tuples of (x, y) values as parameters, representing the coordinates of the vertices of a triangle. The function should calculate the area of the triangle using the given coordinates and return the result rounded to the nearest integer. Assume the coordinates always form a valid triangle.
"""

import math

def calculate_area(vertex1, vertex2, vertex3):
    x1, y1 = vertex1
    x2, y2 = vertex2
    x3, y3 = vertex3
    
    area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    
    return round(area)