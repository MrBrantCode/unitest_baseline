"""
QUESTION:
Create two functions, `celsius_to_fahrenheit(celsius)` and `kelvin_to_fahrenheit(kelvin)`, that convert temperature values from Celsius to Fahrenheit and Kelvin to Fahrenheit respectively. The functions should handle invalid input values, such as non-numeric input, temperatures below -273.15°C or above 1000°C for Celsius, and temperatures below 0K or above 1273.15K for Kelvin. The functions should return the converted temperature value as a float, or an error message as a string for invalid input. The functions should have a time complexity of O(1) and a space complexity of O(1).
"""

def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        if celsius < -273.15 or celsius > 1000:
            return "Invalid Celsius temperature!"
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except ValueError:
        return "Invalid input!"

def kelvin_to_fahrenheit(kelvin):
    try:
        kelvin = float(kelvin)
        if kelvin < 0 or kelvin > 1273.15:
            return "Invalid Kelvin temperature!"
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except ValueError:
        return "Invalid input!"