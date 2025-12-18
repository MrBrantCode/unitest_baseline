"""
QUESTION:
Write a Python function `sector_surface_area` that calculates the surface area of a circular sector and a spherical sector. The function should accept a list of tuples, each containing the radius and central angle of a sector, and an optional boolean parameter `is_spherical` to specify whether the sector is spherical (default: False). The function should return a list of surface areas corresponding to each sector, or None if the central angle exceeds 360 degrees or is less than zero, or if the radius is negative. The function should handle floating point precision issues by rounding the surface area to 2 decimal places. 

The function should be able to handle large inputs without causing memory overflow or exceeding time limits, and should provide appropriate error messages for invalid inputs.
"""

import math

def sector_surface_area(sector_list, is_spherical=False):
    surface_area_list = []

    for sector in sector_list:
        radius, angle = sector

        if angle < 0 or angle > 360 or radius < 0:
            surface_area_list.append(None)
            continue

        if is_spherical:
            # Surface area of a spherical sector = 2πRh
            # where R is the radius of the sphere and h is the height of the sector
            # h can be calculated as R(1-cos(angle))
            h = radius * (1 - math.cos(math.radians(angle)))
            surface_area = 2 * math.pi * radius * h
        else:
            # Surface area of a circular sector = (angle / 360) * π * radius^2
            surface_area = (angle / 360) * math.pi * math.pow(radius, 2)

        surface_area_list.append(round(surface_area, 2))

    return surface_area_list