"""
QUESTION:
Write a function `convert_celsius_to_fahrenheit` that takes an integer temperature in Celsius as input and returns the equivalent temperature in Fahrenheit as a float, rounded to 2 decimal places. The formula to convert Celsius to Fahrenheit is (Celsius * 9/5) + 32.
"""

def convert_celsius_to_fahrenheit(celsius):
    """
    Converts a temperature in Celsius to Fahrenheit.

    Args:
    celsius (int): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit rounded to 2 decimal places.
    """
    return round((celsius * 9/5) + 32, 2)