"""
QUESTION:
Write a function `compute_surface_areas(b, h, l)` that calculates and returns the lateral and total surface areas of a right-angled triangular prism given its base `b`, height `h`, and length `l`. The function should return two values: the lateral surface area (excluding the bases) and the total surface area (including the bases). Assume that the input values are non-negative numbers.
"""

def compute_surface_areas(b, h, l):
   lateral_surface_area = 2 * l * h + b * h
   total_surface_area = lateral_surface_area + 2 * l * b
   return lateral_surface_area, total_surface_area