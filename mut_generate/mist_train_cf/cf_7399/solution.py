"""
QUESTION:
Create a function `convert_fahrenheit_to_celsius(temperature)` that takes a temperature in Fahrenheit as input and returns the equivalent temperature in Celsius, rounded to the nearest whole number. The input temperature must be between -10000 and 10000 (inclusive), and the converted temperature must be within the range of -1000 and 1000 (inclusive). If the input temperature or the converted temperature is outside the valid range, return "Invalid temperature".
"""

def convert_fahrenheit_to_celsius(temperature):
    if temperature < -10000 or temperature > 10000:
        return "Invalid temperature"
    celsius = round((temperature - 32) * 5/9)
    if celsius < -1000 or celsius > 1000:
        return "Invalid temperature"
    return celsius