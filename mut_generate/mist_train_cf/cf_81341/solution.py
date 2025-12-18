"""
QUESTION:
Calculate the distance between two ships after 3 hours of travel. The ship heading east has varying speed due to wind direction and intensity, while the ship heading north travels at a constant speed but deviates from its path occasionally due to obstacles. 

Function name: `calculate_distance`. 

Input: 
- `speed_east`: a list of 3 integers representing the speed of the ship heading east in km/hr for each hour, affected by wind direction and intensity.
- `speed_north`: a list of 3 integers representing the speed of the ship heading north in km/hr for each hour.
- `obstacle_path`: a list of 3 integers representing the obstacle direction deviation (either left or right) for the ship heading north.
- `wind_direction_intensity`: a list of 3 floats representing the wind direction and intensity for the ship heading east (positively eastward and negatively westward).

Output: The distance between the two ships after 3 hours of travel in kilometers.
"""

import math

def calculate_distance(speed_east, speed_north, obstacle_path, wind_direction_intensity):
    ship_east_pos = sum([wind_direction_intensity[i]*speed_east[i] for i in range(3)])
    ship_north_pos = sum([speed_north[i] for i in range(3)])
    for i in range(3):
        if obstacle_path[i] == -1:
            ship_north_pos = -ship_north_pos
    return math.sqrt(ship_east_pos**2 + ship_north_pos**2)