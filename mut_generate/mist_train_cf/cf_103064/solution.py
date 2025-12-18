"""
QUESTION:
Create a function `celsius_to_fahrenheit` that takes a temperature value in Celsius as input, which can be either a single number or a list of numbers. The function should return the corresponding temperature value(s) in Fahrenheit, using a lambda expression. The function should work with both single values and lists of values.
"""

def celsius_to_fahrenheit(temperature):
    if isinstance(temperature, list):
        return list(map(lambda x: (x * 9/5) + 32, temperature))
    else:
        return (temperature * 9/5) + 32