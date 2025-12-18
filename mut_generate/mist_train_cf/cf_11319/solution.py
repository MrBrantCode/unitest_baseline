"""
QUESTION:
Calculate the distance between two points in 3-dimensional space and round the result to two decimal places. The function, `calculate_distance`, should take in two tuples representing the x, y, z coordinates of the two points and return the distance and the vector components as a tuple (distance, (x, y, z)).
"""

import math

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points in 3-dimensional space and round the result to two decimal places.
    
    Args:
        point1 (tuple): The x, y, z coordinates of the first point.
        point2 (tuple): The x, y, z coordinates of the second point.
    
    Returns:
        tuple: A tuple containing the distance and the vector components as (distance, (x, y, z)).
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Calculate the differences in x, y, z coordinates
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    
    # Calculate the distance using the distance formula
    distance = math.sqrt(dx**2 + dy**2 + dz**2)
    
    # Round the distance to two decimal places
    distance = round(distance, 2)
    
    # Return the distance and the vector components
    return distance, (dx, dy, dz)