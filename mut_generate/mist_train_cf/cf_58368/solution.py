"""
QUESTION:
Create a function named `calculate_volume` that takes the shape and corresponding dimensions as input parameters and returns the volume of the shape. The function should support three shapes: 'cube', 'rectangular prism', and 'cylinder'. For a 'cube', the function should take one dimension (side length). For a 'rectangular prism', the function should take three dimensions (length, width, and height). For a 'cylinder', the function should take two dimensions (radius and height). The function should return an error message if the shape is not recognized or if the required dimensions are not provided.
"""

import math

def calculate_volume(shape, dimension1, dimension2=None, dimension3=None):
    if shape.lower() == 'cube':
        volume = dimension1**3
    elif shape.lower() == 'rectangular prism':
        if dimension2 != None and dimension3 != None: 
            volume = dimension1 * dimension2 * dimension3
        else:
            return 'All three dimensions are required for rectangular prism'
    elif shape.lower() == 'cylinder':
        if dimension2 != None: 
            volume = math.pi * (dimension1**2) * dimension2
        else:
            return 'Both radius and height are required for cylinder'
    else:
        return 'Invalid shape'
    return volume