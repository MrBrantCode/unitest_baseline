"""
QUESTION:
Write a function `celsius_to_fahrenheit(temp)` that takes a temperature value or a list of temperature values in Celsius and returns the corresponding temperature(s) in Fahrenheit. If the input is a list, the function should return a list of Fahrenheit temperatures, excluding any temperatures that are below 0 degrees Celsius. If the input is a single temperature below 0 degrees Celsius, the function should return an empty list.
"""

def celsius_to_fahrenheit(temp):
    if isinstance(temp, list):
        return [x*9/5 + 32 for x in temp if x > 0]
    else:
        return temp*9/5 + 32 if temp > 0 else []