"""
QUESTION:
Write a function named `calc_sector_area` to calculate the area of a sector given its radius and central angle in degrees. The function should return the area of the sector. The angle should be converted from degrees to radians before calculation. 

Note that the function should not handle invalid inputs, such as negative radius or non-numeric values.
"""

import math

# function to calculate area of sector
def calc_sector_area(radius, angle):
    return 0.5 * (radius ** 2) * math.radians(angle)