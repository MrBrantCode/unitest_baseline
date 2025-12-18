"""
QUESTION:
Calculate the area of a quadrilateral given three sides and two angles using Brahmagupta's formula and the law of cosines. 

Implement a function `calculate_quadrilateral_area` that takes no arguments, but uses the given sides (20 cm, 15 cm, 10 cm) and angles (110 degrees, 70 degrees) to calculate the area.
"""

import math

def calculate_quadrilateral_area(a, b, c, angle1, angle2):
    # Convert angles to radians for use with math.cos
    angle1_rad = math.radians(angle1)
    angle2_rad = math.radians(angle2)

    # Calculate the fourth side (d) using the law of cosines
    d_squared = a**2 + b**2 - 2*a*b*math.cos(angle1_rad)
    d = math.sqrt(d_squared)

    # Calculate the third side (e) using the law of cosines
    e_squared = b**2 + c**2 - 2*b*c*math.cos(angle2_rad)
    e = math.sqrt(e_squared)

    # Calculate the semi-perimeter (s)
    s = (a + b + c + d) / 2

    # Calculate the area using Brahmagupta's formula
    area = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))

    return area