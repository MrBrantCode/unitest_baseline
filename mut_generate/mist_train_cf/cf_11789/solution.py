"""
QUESTION:
Write a function `celsius_to_fahrenheit` that takes a single floating-point number representing a temperature in Celsius. The function should return the equivalent temperature in Fahrenheit, rounded to two decimal places. If the input temperature is less than absolute zero (-273.15°C), the function should return an error message or indicator instead.
"""

def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature in Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
    
    Returns:
        float: Temperature in Fahrenheit, or an error message if input is below absolute zero.
    """
    if celsius < -273.15:
        return "Invalid temperature"
    else:
        fahrenheit = round((celsius * 9/5) + 32, 2)
        return fahrenheit