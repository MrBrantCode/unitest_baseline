"""
QUESTION:
Create a function named `cross_product` that takes two 3-dimensional vectors `v1` and `v2` as input, calculates their cross product, and returns a vector with a magnitude greater than 5. If the magnitude of the cross product is less than or equal to 5, scale the vector to meet the requirement.
"""

import numpy as np
def cross_product(v1, v2):
    # convert the input vectors to numpy arrays
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    # calculate the cross product using the matrix formula
    cross = np.cross(v1, v2)
    
    # calculate the magnitude of the resultant vector
    mag = np.linalg.norm(cross)
    
    # if the magnitude is less than or equal to 5, scale the vector to make its magnitude greater than 5
    if mag <= 5:
        cross = cross * (5 / mag)
    
    return cross