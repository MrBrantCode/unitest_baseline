"""
QUESTION:
Create a function called `sphere_properties` that takes one parameter: the radius of a sphere. The function should return three values: the area of a circle with the given radius, the surface area of the sphere, and the volume of the sphere. Use the mathematical constant pi (π) in your calculations. The function should handle edge cases where the radius is negative or zero, and return an error message for a negative radius and zeros for all calculations when the radius is zero. Consider adding error handling to validate user inputs.
"""

import math

def sphere_properties(radius):
    if radius < 0:
        return "Invalid radius. Must be positive."
    elif radius == 0:
        return 0, 0, 0
    else:
        area = 4 * math.pi * pow(radius, 2)
        volume = (4/3) * math.pi * pow(radius, 3)
        circle_area = math.pi * pow(radius,2)
    return circle_area, area, volume