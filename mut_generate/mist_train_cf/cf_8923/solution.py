"""
QUESTION:
Create a function named `calculate_distance` that takes two 3D points as input and returns the squared distance between them. The function should not use the standard distance formula and instead use the Pythagorean theorem to calculate the distance in each dimension and then combine the results. The input points are represented as tuples of three integers, and the function should return an integer value representing the squared distance.
"""

def calculate_distance(point1, point2):
    distance_x = abs(point2[0] - point1[0])
    distance_y = abs(point2[1] - point1[1])
    distance_z = abs(point2[2] - point1[2])
    
    distance_2d = (distance_x**2) + (distance_y**2)
    distance_3d = (distance_2d) + (distance_z**2)
    
    return distance_3d