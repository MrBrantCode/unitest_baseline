"""
QUESTION:
Create a function `calc_sector_areas` that accepts a list of tuples as input, where each tuple contains the radius and central angle of a circular sector in degrees. The function should return a list of surface areas corresponding to each sector, calculated using the formula `0.5 * r^2 * θ`, where `r` is the radius and `θ` is the central angle in radians. If any sector has a central angle that exceeds 360 degrees or is negative, the function should return `None` for that particular sector. The function should also handle invalid inputs, such as negative radii or non-numeric values, and return an error message. The surface areas should be rounded to 2 decimal places.
"""

import math

def calc_sector_areas(sector_list):
    areas = []
    for sector in sector_list:
        if not isinstance(sector, tuple) or len(sector) != 2:
            return "Error: Invalid sector format."
        radius, angle = sector
        if not (isinstance(radius, (int, float)) and isinstance(angle, (int, float))):
            return "Error: Invalid input type."
        if radius < 0:
            return "Error: Radius cannot be negative."
        elif angle < 0 or angle > 360:
            areas.append(None)
        else:
            area = 0.5 * (radius ** 2) * math.radians(angle)
            areas.append(round(area, 2))
    return areas