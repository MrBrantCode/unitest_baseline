"""
QUESTION:
Create a function named `calculate_distance` that takes four parameters: `x`, `y`, `a`, and `b`, representing the coordinates of two points. The function should calculate and return the Manhattan distance between the points `(x, y)` and `(a, b)`, handling both positive, negative, and zero coordinates, as well as floating-point numbers.
"""

def calculate_distance(x, y, a, b):
    return abs(x - a) + abs(y - b)