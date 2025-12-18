"""
QUESTION:
Create a function "calculate_area" that takes a list of tuples representing the coordinates of the vertices of a polygon and returns the area of the polygon. The function should raise a custom exception "InvalidPolygonException" if the given list of tuples does not represent a valid polygon (i.e., it has less than 3 vertices).
"""

class InvalidPolygonException(Exception):
    pass

def calculate_area(vertices):
    if len(vertices) < 3:
        raise InvalidPolygonException("A polygon should have at least 3 vertices")

    area = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2

    return area