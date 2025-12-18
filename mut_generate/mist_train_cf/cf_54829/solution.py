"""
QUESTION:
Create a function called `truncated_pyramid_volume` that takes five parameters: the length and width of the base, the length and width of the top, and the height of a truncated pyramid. Using the formula V = 1/3 * height * (base_area + top_area + sqrt(base_area * top_area)), calculate the volume of the pyramid where base_area is the product of the base length and width, and top_area is the product of the top length and width.
"""

from math import sqrt

def truncated_pyramid_volume(base_length, base_width, top_length, top_width, height):
    base_area = base_length * base_width
    top_area = top_length * top_width
    volume = 1/3 * height * (base_area + top_area + sqrt(base_area * top_area))
    return volume