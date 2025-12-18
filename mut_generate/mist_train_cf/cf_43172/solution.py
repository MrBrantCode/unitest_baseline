"""
QUESTION:
Create a function `celsius_to_fahrenheit` that takes a temperature in Celsius as input and returns the converted temperature in Fahrenheit using the formula F = (9/5)C + 32. The function should be able to handle both integer and floating-point input values.
"""

def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature in Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    return (9/5) * celsius + 32