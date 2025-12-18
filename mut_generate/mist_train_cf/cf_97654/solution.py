"""
QUESTION:
Write a function `celsius_to_fahrenheit(celsius)` that takes a single Celsius temperature as input, converts it to Fahrenheit, and returns the result. The function should handle non-numeric inputs and temperatures up to 1000 degrees Celsius.
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