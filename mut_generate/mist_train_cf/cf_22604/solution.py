"""
QUESTION:
Create a function `fahrenheit_to_celsius` that takes a Fahrenheit temperature input from the user, converts it to Celsius, and prints the result. If the input is not a valid number, the function should display an error message and prompt the user to enter a valid temperature. The Celsius temperature should be displayed with four decimal places.
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit temperature to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 4)