"""
QUESTION:
Write a function `celsius_to_fahrenheit(celsius)` that takes a single Celsius temperature as input and returns the corresponding Fahrenheit temperature. The function should include error handling for non-numeric inputs and should be able to handle input temperatures up to 1000 degrees Celsius.
"""

def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
    except ValueError:
        return "Invalid input"
    if celsius > 1000:
        return "Temperature too high"
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit