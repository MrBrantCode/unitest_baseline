"""
QUESTION:
Create a function `convert_temperature` that takes a temperature value and its unit as input, where the unit can be Celsius (C), Fahrenheit (F), Kelvin (K), or Rankine (R). The function should convert the temperature to Fahrenheit, round the result to the nearest integer without using built-in rounding functions, and return the converted temperature and unit. If the input unit is invalid, the function should return an error message. The function should also handle extreme temperatures, such as below absolute zero or above 1000°C, and return appropriate error or warning messages.
"""

import math

def convert_temperature(temperature, unit):
    valid_units = ["C", "F", "K", "R"]

    temperature = temperature.strip()
    value, unit = temperature[:-1], temperature[-1].upper()

    if unit not in valid_units:
        return "Invalid unit: {}".format(unit)

    try:
        value = float(value)
    except ValueError:
        return "Invalid temperature: {}".format(value)

    if unit == "C":
        temperature = value * 9/5 + 32
    elif unit == "F":
        temperature = value
    elif unit == "K":
        temperature = value - 273.15
        temperature = temperature * 9/5 + 32
    elif unit == "R":
        temperature = value - 459.67

    if temperature < -459.67:
        return "Invalid temperature: below absolute zero"

    if temperature > 1832:
        return "Warning: Temperature is very high"

    temperature = int(temperature + 0.5)

    return "{}°F".format(temperature)