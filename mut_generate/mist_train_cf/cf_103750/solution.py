"""
QUESTION:
Create a function `convert_temperature` that takes a temperature and a scale as input, where the scale can be "C" for Celsius, "K" for Kelvin, or "R" for Rankine. The function should convert the temperature to Fahrenheit and return the result rounded to the nearest integer.
"""

def convert_temperature(temperature, scale):
    if scale == "C":
        return round((temperature * 9/5) + 32)
    elif scale == "K":
        return round((temperature - 273.15) * 9/5 + 32)
    elif scale == "R":
        return round(temperature - 459.67)