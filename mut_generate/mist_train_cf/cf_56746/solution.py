"""
QUESTION:
Calculate the area of a parallelogram given its base length, slant height, and the angle between them. 

Function name: parallelogram_area
Input parameters: base_length, slant_height, angle_in_degrees
Restrictions: angle_in_degrees is the angle between the base and the slant height, and is given in degrees.
"""

import math

def parallelogram_area(base_length, slant_height, angle_in_degrees):
    # Convert angle from degrees to radians
    angle_in_radians = math.radians(angle_in_degrees)
    
    # Calculate the perpendicular height
    height = math.sin(angle_in_radians) * slant_height
    
    # Calculate the area of the parallelogram
    area = base_length * height
    
    return area