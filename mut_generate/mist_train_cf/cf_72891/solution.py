"""
QUESTION:
Write a function `calc_surface_area` that calculates the surface area of a truncated pyramid (frustum) given its top base area, bottom base area, and height. The function should also calculate the slant height of the truncated pyramid based on the given dimensions. Assume that the bases of the truncated pyramid are circular.
"""

import math

def calc_surface_area(top_base_area, bottom_base_area, top_base, bottom_base, height):
    slant_height = math.sqrt((bottom_base - top_base)**2 / 4 + height**2)
    return top_base_area + bottom_base_area + 1/2 * (bottom_base + top_base) * slant_height