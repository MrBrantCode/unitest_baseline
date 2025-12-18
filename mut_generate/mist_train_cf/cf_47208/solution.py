"""
QUESTION:
Create a function `convert_temp_scale` that takes two parameters: `fahrenheit` (temperature in Fahrenheit scale) and `scale` (the target temperature scale, either 'celsius', 'kelvin', or 'rankine'). The function should convert the given Fahrenheit temperature to the specified scale and return the result. The input `fahrenheit` will be a float and `scale` will be a string.
"""

def convert_temp_scale(fahrenheit, scale):
    if scale == 'celsius':
        return (fahrenheit - 32) * (5 / 9)
    elif scale == 'kelvin':
        return (fahrenheit - 32) * (5 / 9) + 273.15
    elif scale == 'rankine':
        return fahrenheit + 459.67