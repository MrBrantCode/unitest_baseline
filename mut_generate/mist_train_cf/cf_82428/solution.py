"""
QUESTION:
Create a Python function named `frustum_surface_area` that calculates the surface area of a frustum of a pyramid given the base edge length, top edge length, slant height, and height. The function should handle exceptions for invalid inputs. Assume the pyramid is square and use the formula Radius = Edge/sqrt(2) to calculate the radii from the edge lengths.
"""

import math

def frustum_surface_area(base_edge, top_edge, slant_height, height):
    try:
        base_radius = base_edge / math.sqrt(2)
        top_radius = top_edge / math.sqrt(2)

        # calculate the areas
        base_area = math.pi * (base_radius ** 2)
        top_area = math.pi * (top_radius ** 2)
        lateral_area = math.pi * (base_radius+top_radius) * slant_height

        # the total surface area is the sum of the base, top, and lateral areas
        total_surface_area = base_area + top_area + lateral_area

        return total_surface_area
    
    except Exception as e:
        return str(e)  # convert the exception into a string and return it