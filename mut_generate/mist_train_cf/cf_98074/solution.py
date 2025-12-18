"""
QUESTION:
Write a function `calculate_diameter_ratio` that calculates the diameter of Jupiter relative to Earth's diameter, taking into account the temperature variation and specific gravity of both planets. The function should use the formula that incorporates the ratio of the specific heats of the gases in their atmospheres.
"""

import math

def calculate_diameter_ratio(earth_diameter, jupiter_diameter, earth_specific_gravity, jupiter_specific_gravity, 
                             earth_ratio_of_specific_heats, jupiter_ratio_of_specific_heats, 
                             jupiter_surface_temperature_variation, jupiter_surface_temperature, earth_surface_temperature):
    
    jupiter_avg_radius = jupiter_diameter / 2
    earth_avg_radius = earth_diameter / 2
    jupiter_volume = (4/3) * math.pi * jupiter_avg_radius**3
    earth_volume = (4/3) * math.pi * earth_avg_radius**3
    jupiter_mass = jupiter_volume * jupiter_specific_gravity
    earth_mass = earth_volume * earth_specific_gravity
    
    jupiter_ratio_of_specific_heats_factor = jupiter_ratio_of_specific_heats / (jupiter_ratio_of_specific_heats - 1)
    earth_ratio_of_specific_heats_factor = earth_ratio_of_specific_heats / (earth_ratio_of_specific_heats - 1)
    
    jupiter_c_sound = math.sqrt(jupiter_ratio_of_specific_heats_factor * 8.31 * jupiter_surface_temperature / jupiter_specific_gravity)
    earth_c_sound = math.sqrt(earth_ratio_of_specific_heats_factor * 8.31 * earth_surface_temperature / earth_specific_gravity)
    
    jupiter_diameter_ratio = jupiter_diameter / earth_diameter
    jupiter_diameter_ratio_with_temp = jupiter_diameter_ratio * (jupiter_c_sound / earth_c_sound) * ((jupiter_surface_temperature + jupiter_surface_temperature_variation) / jupiter_surface_temperature)**0.5 * (earth_specific_gravity / jupiter_specific_gravity)**0.5
    
    return jupiter_diameter_ratio_with_temp