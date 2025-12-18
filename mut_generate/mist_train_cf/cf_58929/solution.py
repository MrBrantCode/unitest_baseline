"""
QUESTION:
Write a function `sector_areas(section_list, sector_type)` that takes a list of sectors and the type of sector, and returns a list of areas for each sector in the input list. Each sector in the list is a tuple where the first element is the radius and the second element is the central angle in degrees. The `sector_type` parameter is a string, either "circular" or "spherical". If the sector type is neither "circular" nor "spherical", the function should return an error message. If a sector has an invalid radius or central angle, its area should be `None` in the output list.
"""

import math

def sector_areas(section_list, sector_type):
    if sector_type not in ["circular", "spherical"]:
        return "Invalid sector type! Please choose either 'circular' or 'spherical'."

    area_list = []

    for sector in section_list:
        radius = sector[0]
        central_angle = sector[1]

        if central_angle > 360 or central_angle < 0 or radius < 0:
            area_list.append(None)
            continue

        if sector_type == "circular":
            # Formula for area of a circular sector: (central_angle / 360) * PI * radius^2
            area = round((central_angle / 360) * math.pi * math.pow(radius, 2), 2)
        else:
            # Formula for area of a spherical sector: 2 * PI * radius^2 * (1 - cos(central_angle / 2))
            # Convert the central angle into radians as the math.cos function expects radians
            central_angle = math.radians(central_angle)
            area = round(2 * math.pi * math.pow(radius, 2) * (1 - math.cos(central_angle / 2)), 2)
        
        area_list.append(area)

    return area_list