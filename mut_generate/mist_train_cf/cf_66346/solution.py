"""
QUESTION:
Compute the surface area of circular and spherical sectors given their radii and central angles. 

The function, `compute_sector_surface_area`, should take a list of tuples as input, where each tuple contains the radius and central angle of a sector. It should return a list of tuples, where each tuple contains the surface areas of the circular and spherical sectors corresponding to the input sector. 

If the central angle of a sector is less than 0 or greater than 360 degrees, the function should return `None` for that sector. The function should also handle negative radii and provide an error message. 

The surface areas should be rounded to 2 decimal places if the radius is a floating point number with more than 2 decimal places. The function should be optimized to handle large inputs efficiently without triggering memory overflow or surpassing time limits.
"""

import math

def compute_sector_surface_area(sectors):
    results = []
    for sector in sectors:
        radius, angle = sector
        if not (0 <= angle <= 360) or radius < 0:
            results.append(None)
            continue
        circle_sector_area = (angle/360) * (math.pi * radius * radius)
        spherical_sector_area = angle/360 * 4 * math.pi * radius * radius
        results.append((round(circle_sector_area, 2), round(spherical_sector_area, 2)))
    return results