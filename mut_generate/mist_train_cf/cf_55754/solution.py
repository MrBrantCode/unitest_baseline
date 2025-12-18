"""
QUESTION:
Write a function called `calculate_actual_distance` that takes two parameters: `map_scale` (the number of miles per inch on the map) and `map_length` (the length on the map in inches). The function should return the actual distance represented by the map length in miles.
"""

def calculate_actual_distance(map_scale, map_length):
    """
    This function calculates the actual distance represented by the map length in miles.

    Parameters:
    map_scale (float): The number of miles per inch on the map.
    map_length (float): The length on the map in inches.

    Returns:
    float: The actual distance represented by the map length in miles.
    """
    return map_scale * map_length