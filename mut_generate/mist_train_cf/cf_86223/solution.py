"""
QUESTION:
Write a function called "calculate_distance" that takes in two points in three-dimensional space as input, where each point is a tuple of three integers, and returns the distance between them as a float. The solution should have a time complexity of O(1), cannot use the standard distance formula directly, and cannot use any mathematical functions or libraries.
"""

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points in three-dimensional space.

    Args:
        point1 (tuple): The first point, represented as a tuple of three integers.
        point2 (tuple): The second point, represented as a tuple of three integers.

    Returns:
        float: The distance between the two points.
    """
    distance_squared = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    return distance_squared ** 0.5