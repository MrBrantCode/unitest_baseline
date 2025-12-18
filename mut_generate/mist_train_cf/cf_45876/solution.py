"""
QUESTION:
Write a function called `is_fragmented_by_plane` that determines whether a set of 4 unique points in R^3 space can be fragmented by a plane into at least two subsets, each containing at least one point.
"""

import numpy as np

def is_fragmented_by_plane(points):
    # generate all possible combinations of 3 points to create a plane
    for p1, p2, p3 in combinations(points, 3):
        # calculate the normal vector of the plane
        v1 = p2 - p1
        v2 = p3 - p1
        normal = np.cross(v1, v2)
        
        # calculate the dot product of the normal vector and each point
        dot_products = [np.dot(normal, point - p1) for point in points]
        
        # check if the points are on different sides of the plane
        if any(dot_product > 0 for dot_product in dot_products) and any(dot_product < 0 for dot_product in dot_products):
            return True
            
    return False