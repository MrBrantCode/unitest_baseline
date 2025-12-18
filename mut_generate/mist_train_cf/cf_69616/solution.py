"""
QUESTION:
Write a function called surface_area that calculates the surface area of one or more circular sectors. The function should accept a list of tuples, where each tuple contains the radius and central angle of a sector in that order. The function should return a list of surface areas corresponding to each sector, or None if the central angle exceeds 360 degrees or is less than 0 degrees for that sector. The function should also return 'Invalid input.' for any sector with invalid input, such as a negative radius or a non-numeric angle. The surface areas should be rounded to 2 decimal places.
"""

import math

def surface_area(sector_data):
    # calculate area of a sector
    def cal_area_sector(radius, angle):
        if angle < 0 or angle > 360:
            return None
        return round((math.pi * radius ** 2) * (angle/360), 2)

    surface_areas = []
    for data in sector_data:
        # Check if input is valid
        if len(data) != 2 or type(data[0]) not in (int, float) or type(data[1]) not in (int, float) or data[0] < 0:
            surface_areas.append('Invalid input.')
            continue
        else:
            radius = data[0]
            angle = data[1]
            surface_areas.append(cal_area_sector(radius, angle))
    return surface_areas