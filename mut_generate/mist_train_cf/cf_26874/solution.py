"""
QUESTION:
Determine the relationship between two circles in a 2D plane based on their positions and radii. The relationship can be one of "None", "More", or "One". 

Write a function `circleRelationship` that takes the coordinates (x1, y1) and radius (r1) of the first circle, and the coordinates (x2, y2) and radius (r2) of the second circle as input. The function should return a string representing the relationship between the two circles. The coordinates and radii are all non-negative double values.
"""

def circle_relationship(x1, y1, r1, x2, y2, r2):
    """
    Determine the relationship between two circles in a 2D plane based on their positions and radii.

    Args:
        x1 (float): The x-coordinate of the center of the first circle.
        y1 (float): The y-coordinate of the center of the first circle.
        r1 (float): The radius of the first circle.
        x2 (float): The x-coordinate of the center of the second circle.
        y2 (float): The y-coordinate of the center of the second circle.
        r2 (float): The radius of the second circle.

    Returns:
        str: The relationship between the two circles, which can be "None", "More", or "One".
    """
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if dist > r1 + r2:
        return "None"
    elif x1 == x2 and y1 == y2 and r1 == r2:
        return "More"
    elif dist < r1 and dist + r2 == r1:
        return "One"
    elif dist < r2 and dist + r1 == r2:
        return "One"
    else:
        return "None"