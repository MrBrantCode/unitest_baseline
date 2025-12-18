"""
QUESTION:
Write a function named `calculate_actual_distance` that takes two parameters: `scale` (the scale of the map in the format 1:x) and `distance_on_map` (the distance between the cities on the map in centimeters). The function should calculate the actual distance between the cities in kilometers, rounded to the nearest hundredth, and return the result. Assume the scale is given as a ratio where the first number is always 1.
"""

def calculate_actual_distance(scale, distance_on_map):
    """
    Calculate the actual distance between two cities based on the map scale.

    Args:
        scale (int): The scale of the map in the format 1:x.
        distance_on_map (float): The distance between the cities on the map in centimeters.

    Returns:
        float: The actual distance between the cities in kilometers, rounded to the nearest hundredth.
    """
    actual_distance = distance_on_map * scale / 100000  # Divide by 100000 to convert cm to km
    return round(actual_distance, 2)