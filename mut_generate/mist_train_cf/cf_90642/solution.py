"""
QUESTION:
Create a function named `calculate_distance` that takes two points in three-dimensional space as input, where each point is represented as a tuple of three integers. The function should return the squared distance between the two points without using the standard distance formula.
"""

def calculate_distance(point1, point2):
    distance_x = abs(point2[0] - point1[0])
    distance_y = abs(point2[1] - point1[1])
    distance_z = abs(point2[2] - point1[2])
    
    distance_2d = (distance_x**2) + (distance_y**2)
    distance_3d = (distance_2d) + (distance_z**2)
    
    return distance_3d