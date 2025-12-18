"""
QUESTION:
Write a function `celsius_to_fahrenheit` that takes a temperature in degrees Celsius as input and returns the equivalent temperature in degrees Fahrenheit. The function should handle invalid inputs by returning "Invalid input" for non-numeric or negative values.
"""

def celsius_to_fahrenheit(celsius):
    if isinstance(celsius, (int, float)) and celsius >= 0:
        return celsius * 9/5 + 32
    else:
        return "Invalid input"