"""
QUESTION:
Write a function `calculate_actual_distance` that takes the scale of a map and the distance between two cities on the map as input and returns the actual distance between the two cities in kilometers. The scale is given as a ratio of 1:x and the distance on the map is given in centimeters. The function should round the actual distance to the nearest hundredth.
"""

def calculate_actual_distance(scale, distance_on_map):
    """
    Calculate the actual distance between two cities given the scale of a map and the distance between the cities on the map.

    Args:
    scale (int): The scale of the map as a ratio of 1:x.
    distance_on_map (float): The distance between the cities on the map in centimeters.

    Returns:
    float: The actual distance between the cities in kilometers, rounded to the nearest hundredth.
    """
    actual_distance = distance_on_map * scale / 100000 # Divide by 100000 to convert cm to km
    return round(actual_distance, 2)