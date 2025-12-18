"""
QUESTION:
Create a function named `convert_temperature` that takes in two parameters: `temperature` (a floating-point number) and `scale` (a string representing the unit of temperature, where "C" denotes Celsius, "K" denotes Kelvin, and "R" denotes Rankine). The function should convert the input temperature to Fahrenheit and return the result rounded to the nearest integer.
"""

def convert_temperature(temperature, scale):
    if scale == "C":
        return round((temperature * 9/5) + 32)
    elif scale == "K":
        return round((temperature - 273.15) * 9/5 + 32)
    elif scale == "R":
        return round(temperature - 459.67)