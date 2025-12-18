"""
QUESTION:
Given a cube with a side length of 14cm, find the dimensions of a cuboid with the same surface area, where the length of the cuboid is twice its width and its height is half its width. Implement a function `calculate_cuboid_dimensions(cube_side)` that returns the accurate dimensions (length, width, and height) of the cuboid.
"""

import math

def calculate_cuboid_dimensions(cube_side):
    cube_surface_area = 6 * cube_side**2      # calculate surface area of cube
    w = math.sqrt(cube_surface_area / 7.5)    # calculate w using derived equation
    l = 2 * w                                 # calculate l
    h = w / 2                                 # calculate h
    return l, w, h                            # return dimensions of the cuboid