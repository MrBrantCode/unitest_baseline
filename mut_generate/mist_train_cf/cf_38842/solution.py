"""
QUESTION:
Implement a function `find_closest_color(target_color, color_set)` that takes a target color as an RGB tuple and a set of predefined colors as a list of RGB tuples, and returns the closest matching color from the color set to the target color. The distance between two colors is calculated using the Euclidean distance formula in the RGB color space. The RGB values are floating point numbers between 0 and 1.
"""

import math

def find_closest_color(target_color, color_set):
    def distance(color1, color2):
        return math.sqrt((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2)

    closest_color = color_set[0]
    min_distance = distance(target_color, color_set[0])

    for color in color_set[1:]:
        dist = distance(target_color, color)
        if dist < min_distance:
            min_distance = dist
            closest_color = color

    return closest_color