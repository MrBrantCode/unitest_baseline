"""
QUESTION:
Write a function named `find_closest_kelvin_fahrenheit` that takes a dictionary of Kelvin to Fahrenheit conversion rates and a target Kelvin temperature as input. The function should find the closest Kelvin temperature to the target temperature in the dictionary and return its equivalent Fahrenheit temperature rounded to the nearest hundredth.
"""

def find_closest_kelvin_fahrenheit(kelvin_fahrenheit, target_kelvin):
    """
    Find the closest Kelvin temperature to the target temperature in the dictionary 
    and return its equivalent Fahrenheit temperature rounded to the nearest hundredth.

    Args:
        kelvin_fahrenheit (dict): A dictionary of Kelvin to Fahrenheit conversion rates.
        target_kelvin (int): The target Kelvin temperature.

    Returns:
        float: The Fahrenheit temperature of the closest Kelvin temperature.
    """
    closest_kelvin = min(kelvin_fahrenheit, key=lambda x: abs(x-target_kelvin))
    return round(kelvin_fahrenheit[closest_kelvin], 2)