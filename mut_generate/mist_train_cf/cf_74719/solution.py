"""
QUESTION:
Create a function named `sector_areas` that calculates the surface area of circular and spherical sectors. The function should accept two parameters: `sector_list` and `sector_type`. 

- `sector_list` is a list of tuples where each tuple contains the radius and central angle of a sector. 
- `sector_type` is a string indicating the type of sector, which can be either "circular" or "spherical".

If the central angle exceeds 360 degrees or is negative, or if the radius is negative, the function should return None for that particular sector. 

The function should also handle invalid inputs, such as non-numeric radius or angle values, and return an appropriate error message. 

The function should round the surface area to 2 decimal places to avoid floating point precision issues. 

The function should return a list of surface areas corresponding to each sector in the input list.
"""

import math

def sector_areas(sector_list, sector_type="circular"):
    if sector_type not in ["circular", "spherical"]:
        return "Invalid sector type! Please choose either 'circular' or 'spherical'."

    area_list = []
    
    for sector in sector_list:
        radius = sector[0]
        central_angle = sector[1]
        
        if central_angle > 360 or central_angle < 0 or radius < 0:
            area_list.append(None)
            continue
        
        if sector_type == "circular":
            area = round((central_angle / 360) * math.pi * math.pow(radius, 2), 2)
        else:
            central_angle = math.radians(central_angle)
            area = round(2 * math.pi * math.pow(radius, 2) * (1 - math.cos(central_angle / 2)), 2)
        
        area_list.append(area)
    
    return area_list