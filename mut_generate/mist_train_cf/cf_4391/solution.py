"""
QUESTION:
Write a function `convert_temp` that takes a string representing a temperature in Celsius and returns the converted temperature in Fahrenheit as a float rounded to two decimal places. The input temperature is a valid number between -273.15 and 1000, may or may not contain leading zeros or a decimal point, and has no leading or trailing spaces.
"""

def convert_temp(temp_celsius):
    """
    This function converts a temperature in Celsius to Fahrenheit.

    Args:
        temp_celsius (str): A string representing a temperature in Celsius.

    Returns:
        float: The converted temperature in Fahrenheit rounded to two decimal places.
    """
    return round(float(temp_celsius) * 9/5 + 32, 2)