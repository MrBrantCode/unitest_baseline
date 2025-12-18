"""
QUESTION:
Write a function named `Compute_Surface_Area` that calculates the total interior surface area of a cylindrical tube. The function should take three parameters: `height`, `outer_rad`, and `inner_rad`, representing the height and the outer and inner radii of the tube, respectively. The formula for the surface area of the tube is (2π * r1 * h + 2π * r1²) - (2π * r2 * h + 2π * r2²). The function should return the calculated surface area.
"""

import math

def Compute_Surface_Area(height, outer_rad, inner_rad):
    return ((2*math.pi*outer_rad*height + 2*math.pi*pow(outer_rad,2)) - (2*math.pi*inner_rad*height + 2*math.pi*pow(inner_rad,2)))