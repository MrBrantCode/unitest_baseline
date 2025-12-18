"""
QUESTION:
Write a function `manhattan_distance` that calculates the Manhattan distance between two points in 3D space. The function should accept two tuples `p1` and `p2` as input, each containing three decimal numbers representing the x, y, and z coordinates of a point. The function should return the Manhattan distance between the two points, rounded to two decimal places.
"""

def manhattan_distance(p1, p2):
    """
    Calculate the Manhattan distance between two points in 3D space.

    Args:
        p1 (tuple): The first point with x, y, and z coordinates.
        p2 (tuple): The second point with x, y, and z coordinates.

    Returns:
        float: The Manhattan distance between the two points, rounded to two decimal places.
    """
    return round(abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2]), 2)