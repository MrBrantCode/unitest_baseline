"""
QUESTION:
Write a function named `manhattan_distance` that calculates the Manhattan distance between two points in a four-dimensional Cartesian coordinate system. The function should take two tuples, each containing four integers representing the X, Y, Z, and W coordinates of a point. The function should return the Manhattan distance between the two points.
"""

def manhattan_distance(point1, point2):
    """
    Calculate the Manhattan distance between two points in a four-dimensional Cartesian coordinate system.
    
    Parameters:
    point1 (tuple): A tuple containing four integers representing the X, Y, Z, and W coordinates of the first point.
    point2 (tuple): A tuple containing four integers representing the X, Y, Z, and W coordinates of the second point.
    
    Returns:
    int: The Manhattan distance between the two points.
    """
    
    # Extract coordinates
    x1, y1, z1, w1 = point1
    x2, y2, z2, w2 = point2
    
    # Calculate Manhattan distance
    distance = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) + abs(w1 - w2)
    
    return distance