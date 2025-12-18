"""
QUESTION:
Write a function named `get_parallelogram_area` that takes six arguments: `ab`, `bc`, `cd`, `da`, `theta1`, and `theta3`, where `ab`, `bc`, `cd`, and `da` represent the lengths of the sides of a parallelogram, and `theta1` and `theta3` are the angles between sides AB and BC, and CD and DA, respectively. The angles can be either acute or obtuse (0 < θ1, θ3 < 180 degrees). The function should return the area of the parallelogram as a float.
"""

import math

def get_parallelogram_area(ab, bc, cd, da, theta1, theta3):
    #Convert theta1 and theta3 from degrees to radians
    theta1 = math.radians(theta1)
    theta3 = math.radians(theta3)
    
    #Calculate the height using sine of the angle and the adjacent side
    height1 = bc * math.sin(theta1)
    height3 = ab * math.sin(theta3)
    
    #If both angles are acute or obtuse, their heights will have same sign, so use one of them as height
    #if one angle is acute and one is obtuse, their heights will have different signs
    #in this case, calculate total height as sum of absolute values of both heights
    if (height1 >= 0 and height3 >=0) or (height1 <= 0 and height3 <= 0):
        height = height1
    else:
        height = abs(height1) + abs(height3)
        
    #Area is base times height
    area = ab*height
    return area