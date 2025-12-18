"""
QUESTION:
Write a function `upmost_vertex(points)` that calculates the minimum bounding rectangle (MBR) enclosing a set of 2D points and returns the maximum y-coordinate of the MBR's vertices. The function takes a list of 2D points as input, where each point is represented as (x, y) coordinates. The MBR is the smallest rectangle aligned with the coordinate axes that completely encloses the given points.
"""

import numpy as np

def upmost_vertex(points):
    MAXD = float('inf')
    MIND = float('-inf')
    
    points = np.asarray(points)
    min_x = min_y = MAXD
    max_x = max_y = MIND
    
    for point in points:
        x, y = point
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    
    return max_y