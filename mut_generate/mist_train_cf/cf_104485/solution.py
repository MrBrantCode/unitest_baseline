"""
QUESTION:
Create a function called `manhattan_distance` that calculates the Manhattan distance between two points (x, y) and (a, b) in a coordinate plane. The function should take four parameters: `x`, `y`, `a`, and `b`, and return the Manhattan distance as an integer. The coordinates can be positive, negative, or zero.
"""

def manhattan_distance(x, y, a, b):
    distance = abs(x - a) + abs(y - b)
    return distance