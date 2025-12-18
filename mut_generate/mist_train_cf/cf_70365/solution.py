"""
QUESTION:
Create a Python function called `equilateral_triangle_in_hemisphere` that takes the radius of a hemisphere as input and returns the area of the largest possible equilateral triangle that can be inscribed within the hemisphere, along with the Cartesian coordinates of the triangle's apexes. The function should assume the hemisphere is centered at (0,0,0) and oriented such that the flat face of the hemisphere is the XY-plane. The function should also handle invalid inputs (radius <= 0) by returning an error message.
"""

import math

def equilateral_triangle_in_hemisphere(radius):
    if radius <= 0:
        return "Error: Radius should be greater than zero."

    # the sidelength of the equilateral triangle that can 
    # be inscribed in a hemisphere is equal to the diameter
    side_length = 2*radius

    # coordinates of the triangle's apexes
    apex_1 = (0, 0, radius) # top of hemisphere
    apex_2 = (-radius/math.sqrt(2), -radius/math.sqrt(2), 0) # bottom left
    apex_3 = (radius/math.sqrt(2), radius/math.sqrt(2), 0) # bottom right

    # calculating area of equilateral triangle 
    area = (math.sqrt(3) / 4) * side_length**2

    return {"Area": area,
            "Apexes": {
                "Apex 1": apex_1,
                "Apex 2": apex_2,
                "Apex 3": apex_3
            }}