"""
QUESTION:
Write a function `circle_properties(area)` that takes the area of a circle as input and returns a 4-tuple containing the circle's circumference, diameter, the surface area of a sphere with the same radius, and the volume of the sphere with the same radius. The function should use 3.1416 as the value for pi and round off the output to two decimal places.
"""

import math

def circle_properties(area):
    # Calculate radius
    radius = math.sqrt(area / math.pi)
    
    # Calculate circumference
    circumference = 2 * math.pi * radius
    
    # Calculate diameter
    diameter = 2 * radius
    
    # Calculate surface area of the sphere
    surface_area_sphere = 4 * math.pi * math.pow(radius, 2)
    
    # Calculate volume of the sphere 
    volume_sphere = (4/3) * math.pi * math.pow(radius, 3)
    
    # Return the rounded off values
    return round(circumference, 2), round(diameter, 2), round(surface_area_sphere, 2), round(volume_sphere, 2)