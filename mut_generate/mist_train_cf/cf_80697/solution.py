"""
QUESTION:
Write a function named `manhattan_distance` that calculates the Manhattan distance between two points in a 2-dimensional Cartesian plane. The function should take two tuples as arguments, each containing two elements representing the x and y coordinates of a point. The function should return the Manhattan distance, which is the sum of the absolute differences of the x and y coordinates. Ensure that the input tuples are validated to contain exactly two elements each.
"""

def manhattan_distance(pointA, pointB):
    """
    Compute Manhattan distance between two points.
    Args:
    pointA: Tuple representing x and y coordinates of the first point.
    pointB: Tuple representing x and y coordinates of the second point.
    Returns:
    Manhattan distance.
    """

    # Ensure input is in correct format
    assert type(pointA) == tuple and len(pointA) == 2, "pointA must be a tuple with two elements"
    assert type(pointB) == tuple and len(pointB) == 2, "pointB must be a tuple with two elements"
    
    # Manhattan distance is just the sum of the absolute differences of the coordinates
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])