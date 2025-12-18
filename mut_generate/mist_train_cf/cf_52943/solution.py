"""
QUESTION:
Calculate the volume of icing needed to cover a doughnut with a uniform coat of icing one millimeter thick. The doughnut is a torus with radii a, b and distance from center of tube to center of torus c. The function volume_of_icing(a, b, c) should return the volume in mm³, rounded to 8 decimal places. The thickness of the icing is the absolute difference between c and a (or c and b).
"""

import math

def volume_of_icing(a, b, c):
    r = abs(c - a)
    return round((2 * math.pi ** 2) * (r ** 2) * c, 8)