"""
QUESTION:
Create a function `calculate_pyramid_volume` that calculates the volume of a pyramid given its base area and height. The function should use the formula `V = (1/3) * base_area * height`. The base area and height must be non-negative, and the function should return an error message if either value is negative. If either the base area or height is zero, the function should return 0, as the volume of a pyramid with no base or no height is 0.
"""

def calculate_pyramid_volume(base, height):
    if base < 0 or height < 0:
        return "Error: Base and height must be zero or positive numbers."
    elif base == 0 or height == 0:
        return 0
    else:
        volume = 1/3 * base * height
        return volume