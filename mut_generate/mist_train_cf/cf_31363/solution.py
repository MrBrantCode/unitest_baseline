"""
QUESTION:
Write a function named `calculate_polygon_vertices` that takes two parameters: `num_sides` (an integer representing the number of sides of a regular polygon) and `radius` (a float representing the radius of the circumscribed circle). The function should return a list of tuples, where each tuple represents the (x, y) coordinates of a vertex of the regular polygon. The vertices should be listed in counterclockwise order.
"""

import math

def calculate_polygon_vertices(num_sides, radius):
    vertices = []
    angle_increment = 2 * math.pi / num_sides
    for i in range(num_sides):
        x = radius * math.cos(i * angle_increment)
        y = radius * math.sin(i * angle_increment)
        vertices.append((x, y))
    return vertices