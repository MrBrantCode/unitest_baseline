"""
QUESTION:
Create a function `celsius_to_fahrenheit` that takes a single Celsius temperature as input and returns the corresponding Fahrenheit temperature. The function should handle error inputs such as non-numeric values and temperatures above 1000 degrees Celsius. The function should convert Celsius to Fahrenheit using the formula `(celsius * 9/5) + 32`.
"""

def celsius_to_fahrenheit(celsius):
    """
    Converts a single Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The Celsius temperature to convert.

    Returns:
        float: The corresponding Fahrenheit temperature, or an error message if the input is invalid.
    """
    try:
        celsius = float(celsius)
    except ValueError:
        return "Invalid input"
    if celsius > 1000:
        return "Temperature too high"
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit