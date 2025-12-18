"""
QUESTION:
Write a function named `manhattan_distance` that calculates the Manhattan distance between two points in a 3D space. The function should take two tuples, each containing three decimal numbers representing the coordinates of a point. The function should return the Manhattan distance rounded to two decimal places.
"""

def manhattan_distance(point1, point2):
    """
    Calculate the Manhattan distance between two points in a 3D space.

    Args:
        point1 (tuple): The coordinates of the first point as a tuple of three decimal numbers.
        point2 (tuple): The coordinates of the second point as a tuple of three decimal numbers.

    Returns:
        float: The Manhattan distance between the two points, rounded to two decimal places.
    """
    return round(abs(point2[0] - point1[0]) + abs(point2[1] - point1[1]) + abs(point2[2] - point1[2]), 2)