"""
QUESTION:
Create a function `circle_properties(radius, angle)` that calculates the area of a circle, its circumference, and the length of the arc for a given angle. The function should take two arguments: `radius` (the radius of the circle) and `angle` (the angle in degrees). It should return the area, circumference, and arc length of the circle if the inputs are valid, or an error message if the inputs are invalid. The function should handle the following restrictions:
- `radius` and `angle` must be numbers.
- `radius` must be non-negative.
- `angle` must be between 0 and 360 (inclusive).
"""

import math

def circle_properties(radius, angle):
    if not (isinstance(radius, (int, float)) and isinstance(angle, (int, float))):
        return "Invalid input: radius and angle must be numbers"
    
    if radius < 0 or angle < 0 or angle > 360:
        return "Invalid input: radius must be non-negative and angle must be between 0 and 360"
    
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    arc_length = (angle / 360) * circumference
    
    return area, circumference, arc_length