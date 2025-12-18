"""
QUESTION:
Create a function named `celsius_to_kelvin` that takes a temperature in Celsius as input and returns the equivalent temperature in Kelvin. The function should handle invalid inputs (temperatures less than absolute zero, -273.15 °C) and return an error message in such cases. The function should be able to handle floating-point numbers and return the result with the same precision.
"""

def celsius_to_kelvin(temp_celsius):
    # if the input temperature is less than absolute zero (−273.15 °C), it's invalid.
    if temp_celsius < -273.15:
        return "Invalid input. Temperature in Celsius should be above -273.15"
    kelvin = temp_celsius + 273.15
    return kelvin