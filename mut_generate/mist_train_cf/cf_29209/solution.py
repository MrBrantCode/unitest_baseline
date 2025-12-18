"""
QUESTION:
Implement the function `pol2cart` that takes two parameters: an array of polar coordinates `shape_pol` of shape (Nnodes, Ndof) and an array of points in the mesh `points`. The function should return an array of Cartesian coordinates `shape_xyz` of shape (Nnodes, Ndof). Note that `Ndof` is assumed to be 2.
"""

import numpy as np

def pol2cart(shape_pol, points):
    r = shape_pol[:, 0]  
    theta = shape_pol[:, 1]  

    x = r * np.cos(theta)  
    y = r * np.sin(theta)  

    shape_xyz = np.column_stack((x, y))  

    return shape_xyz