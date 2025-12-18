"""
QUESTION:
Calculate the surface area of one or multiple circular sectors given their radii and central angles. 

Create a function named `calculate_surface_area` that takes a list of tuples as input, where each tuple contains a radius and a central angle of a sector in degrees. Return a list of surface areas corresponding to each sector. If any sector has a central angle that exceeds 360 degrees, return `None` for that sector. If the input contains invalid values (negative radii or angles, or non-tuple inputs), return an error message.
"""

from math import pi

def calculate_surface_area(sectors):
    if not all(isinstance(i, tuple) and len(i) == 2 for i in sectors):
        return "Invalid input. Please enter a list of tuples, where each tuple contains radius and central angle of a sector."

    surface_areas = []
    for sector in sectors:
        radius, angle = sector
        if radius < 0 or angle < 0:
            return "Invalid input. Radii and angles should be non-negative."
        elif angle > 360:
            surface_areas.append(None)
        else:
            r_squared = radius ** 2
            circle_area = pi * r_squared
            sector_area = circle_area * (angle/ 360)
            surface_areas.append(sector_area)

    return surface_areas