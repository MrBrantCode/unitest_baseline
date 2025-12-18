"""
QUESTION:
Write a function called `distance_from_y_axis` that takes a point on a Cartesian plane as input and returns the distance from the vertical y-axis to that point. The input point should be a tuple of two integers representing the x and y coordinates. The function should return the absolute value of the x-coordinate as the distance.
"""

def distance_from_y_axis(point):
    """
    Calculate the distance from the y-axis to a point on a Cartesian plane.

    Args:
    point (tuple): A tuple of two integers representing the x and y coordinates.

    Returns:
    int: The absolute value of the x-coordinate, representing the distance from the y-axis.
    """
    return abs(point[0])