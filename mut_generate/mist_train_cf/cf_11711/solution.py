"""
QUESTION:
Write a function named `calculate_distance` that calculates the distance between two points using the Pythagorean theorem. The function should take two tuples representing the coordinates of the points as input, and return the distance rounded to two decimal places.
"""

def calculate_distance(pointA, pointB):
    """
    Calculate the distance between two points using the Pythagorean theorem.

    Args:
        pointA (tuple): The coordinates of the first point.
        pointB (tuple): The coordinates of the second point.

    Returns:
        float: The distance between the two points rounded to two decimal places.
    """
    return round(((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** 0.5, 2)