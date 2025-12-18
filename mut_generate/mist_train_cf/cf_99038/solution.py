"""
QUESTION:
Create a function called `generate_pink_shades` that generates `n` different shades of a given pink color, each shade being darker than the previous one. The function should take two parameters: `base_color` (a tuple representing the RGB values of the base pink color) and `n` (the number of shades to generate). The function should return a list of `n` RGB tuples representing the generated shades.
"""

import colorsys

def generate_pink_shades(base_color, n):
    min_darkness = 0.1
    max_darkness = 0.9
    darkness_increment = (max_darkness - min_darkness) / n
    shades = []
    for i in range(n):
        darkness = min_darkness + i * darkness_increment
        # Ensure base color is in correct format for hsv_to_rgb
        if isinstance(base_color[0], int):
            color = colorsys.hsv_to_rgb(base_color[0]/255, base_color[1]/255, base_color[2]/255 * darkness)
        else:
            color = colorsys.hsv_to_rgb(base_color[0], base_color[1], base_color[2] * darkness)
        shades.append(color)
    return shades