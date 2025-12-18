"""
QUESTION:
Create a function called "celsius_to_fahrenheit" that takes a real number representing a temperature in Celsius as input, and returns the equivalent temperature in Fahrenheit rounded to the nearest integer. The function should use the formula (Celsius * 9/5) + 32 to convert Celsius to Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    rounded_fahrenheit = round(fahrenheit)
    return rounded_fahrenheit