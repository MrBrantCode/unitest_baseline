"""
QUESTION:
Write a function `find_closest_fahrenheit` that takes a dictionary of Kelvin to Fahrenheit conversion rates and a target Kelvin temperature as input, and returns the equivalent Fahrenheit temperature of the closest Kelvin temperature to the target, rounded to the nearest hundredth. The function should assume that the input dictionary contains Kelvin temperatures as keys and their corresponding Fahrenheit temperatures as values.
"""

def find_closest_fahrenheit(kelvin_fahrenheit, target_kelvin):
    """
    This function takes a dictionary of Kelvin to Fahrenheit conversion rates and a target Kelvin temperature as input, 
    and returns the equivalent Fahrenheit temperature of the closest Kelvin temperature to the target, 
    rounded to the nearest hundredth.

    Parameters:
    kelvin_fahrenheit (dict): A dictionary containing Kelvin temperatures as keys and their corresponding Fahrenheit temperatures as values.
    target_kelvin (int): The target Kelvin temperature.

    Returns:
    float: The equivalent Fahrenheit temperature of the closest Kelvin temperature to the target, rounded to the nearest hundredth.
    """
    closest_kelvin = min(kelvin_fahrenheit, key=lambda x: abs(x-target_kelvin))
    return round(kelvin_fahrenheit[closest_kelvin], 2)