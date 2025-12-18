"""
QUESTION:
Implement a function `get_window_radius(window, hp_radius)` that calculates the required radius of a window function given the window function value at a specific point `window` and the half power radius `hp_radius`, assuming the window function is symmetric and centered at the origin. The function should return the required radius as a float.
"""

import math

def get_window_radius(window, hp_radius):
    return math.sqrt(-2 * math.log(hp_radius)) / (2 * math.pi * window)