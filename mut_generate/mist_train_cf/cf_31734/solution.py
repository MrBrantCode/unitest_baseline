"""
QUESTION:
Implement a function `angle_conversion_and_differential(angle)` that takes an angle in radians as input and returns a tuple containing the converted angle in degrees within the range of -90 to 90 degrees, and the calculated differential value. The differential value is calculated based on the converted angle using the following rules: 
- If the angle is less than -0.1, the differential is calculated as 89.1 times the angle in degrees plus 43.7.
- If the angle is greater than 0.1, the differential is calculated as 126 times the angle in degrees minus 28.9.
- If the angle is within the range of -0.1 to 0.1, the differential is 0.
"""

import math

def angle_conversion_and_differential(angle):
    angle_degrees = math.degrees(angle)
    
    if angle_degrees < -90:
        angle_degrees = -90
    elif angle_degrees > 90:
        angle_degrees = 90
    
    if angle < -0.1:
        differential = 89.1 * angle_degrees + 43.7
    elif angle > 0.1:
        differential = 126 * angle_degrees - 28.9
    else:
        differential = 0
    
    return (angle_degrees, differential)