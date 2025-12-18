"""
QUESTION:
Develop a function `convert_temp` that takes a string representing a temperature in Fahrenheit and returns the converted temperature in Celsius as a float, rounded to two decimal places. Ensure the function handles cases where the input string cannot be converted to a number.
"""

def convert_temp(temperature):
    try:
        fahrenheit = float(temperature)
        celsius = (fahrenheit - 32) * 5 / 9
        return round(celsius, 2)
    except ValueError:
        return "Invalid input. Temperature must be a number."