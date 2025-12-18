"""
QUESTION:
Write a function named `find_closest_kelvin_fahrenheit` that finds the closest Kelvin temperature to 500 from a given dictionary of Kelvin to Fahrenheit conversion rates and returns the equivalent Fahrenheit temperature rounded to the nearest hundredth. The dictionary keys are Kelvin temperatures and the values are Fahrenheit temperatures. The function should use the dictionary directly and not perform any additional conversions.
"""

def find_closest_kelvin_fahrenheit(kelvin_fahrenheit, target_kelvin):
    """
    Finds the closest Kelvin temperature to the target temperature from a given dictionary 
    of Kelvin to Fahrenheit conversion rates and returns the equivalent Fahrenheit temperature 
    rounded to the nearest hundredth.

    Args:
    kelvin_fahrenheit (dict): A dictionary of Kelvin to Fahrenheit conversion rates.
    target_kelvin (int): The target Kelvin temperature.

    Returns:
    float: The equivalent Fahrenheit temperature of the closest Kelvin temperature.
    """
    closest_kelvin = min(kelvin_fahrenheit, key=lambda x: abs(x-target_kelvin))
    return round(kelvin_fahrenheit[closest_kelvin], 2)