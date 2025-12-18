"""
QUESTION:
Write a function called `calculate_jupiter_diameter_ratio` that calculates the diameter of Jupiter relative to Earth's diameter, taking into account the temperature variation on Jupiter's surface and the specific gravity of both planets. The function should also incorporate the ratio of the specific heats of the gases in their atmospheres. The function should return the diameter ratio. Assume the following constants: Earth's diameter, Jupiter's diameter, Earth's specific gravity, Jupiter's specific gravity, Earth's ratio of specific heats, Jupiter's ratio of specific heats, and Jupiter's surface temperature variation.
"""

import math

def calculate_jupiter_diameter_ratio(
    earth_diameter=12742, 
    jupiter_diameter=142984, 
    earth_specific_gravity=5.52, 
    jupiter_specific_gravity=1.33, 
    earth_ratio_of_specific_heats=1.4, 
    jupiter_ratio_of_specific_heats=1.67, 
    jupiter_surface_temperature_variation=200
):
    """
    Calculate the diameter of Jupiter relative to Earth's diameter, 
    taking into account temperature variation on Jupiter's surface 
    and the specific gravity of both planets, as well as the ratio 
    of the specific heats of the gases in their atmospheres.

    Args:
    earth_diameter (float): Earth's diameter in kilometers.
    jupiter_diameter (float): Jupiter's diameter in kilometers.
    earth_specific_gravity (float): Earth's specific gravity.
    jupiter_specific_gravity (float): Jupiter's specific gravity.
    earth_ratio_of_specific_heats (float): Earth's ratio of specific heats.
    jupiter_ratio_of_specific_heats (float): Jupiter's ratio of specific heats.
    jupiter_surface_temperature_variation (float): Jupiter's surface temperature variation in Celsius.

    Returns:
    float: The diameter ratio of Jupiter to Earth.
    """

    jupiter_avg_radius = jupiter_diameter / 2
    earth_avg_radius = earth_diameter / 2
    jupiter_volume = (4/3) * math.pi * jupiter_avg_radius**3
    earth_volume = (4/3) * math.pi * earth_avg_radius**3
    jupiter_mass = jupiter_volume * jupiter_specific_gravity
    earth_mass = earth_volume * earth_specific_gravity
    jupiter_surface_temperature = 165 # Celsius (average temperature)
    earth_surface_temperature = 15 # Celsius (average temperature)
    
    jupiter_ratio_of_specific_heats_factor = jupiter_ratio_of_specific_heats / (jupiter_ratio_of_specific_heats - 1)
    earth_ratio_of_specific_heats_factor = earth_ratio_of_specific_heats / (earth_ratio_of_specific_heats - 1)
    
    jupiter_c_sound = math.sqrt(jupiter_ratio_of_specific_heats_factor * 8.31 * jupiter_surface_temperature / jupiter_specific_gravity)
    earth_c_sound = math.sqrt(earth_ratio_of_specific_heats_factor * 8.31 * earth_surface_temperature / earth_specific_gravity)
    
    jupiter_escape_velocity = math.sqrt(2 * 6.67e-11 * jupiter_mass / jupiter_avg_radius)
    earth_escape_velocity = math.sqrt(2 * 6.67e-11 * earth_mass / earth_avg_radius)
    
    jupiter_diameter_ratio = jupiter_diameter / earth_diameter
    jupiter_diameter_ratio_with_temp = jupiter_diameter_ratio * (jupiter_c_sound / earth_c_sound) * ((jupiter_surface_temperature + jupiter_surface_temperature_variation) / jupiter_surface_temperature)**0.5 * (earth_specific_gravity / jupiter_specific_gravity)**0.5
    
    return jupiter_diameter_ratio_with_temp