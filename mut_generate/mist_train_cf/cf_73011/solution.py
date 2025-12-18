"""
QUESTION:
Create a function `fahrenheit_to_celsius(fahrenheit)` that takes a temperature in Fahrenheit as input and returns its equivalent in Celsius. The function should be able to handle non-numeric inputs gracefully. Additionally, create a function `interpret_weather(celsius)` that takes a temperature in Celsius as input and returns the corresponding weather condition: 'Cold' if below 0, 'Cool' if between 0-15, 'Warm' if between 16-30, and 'Hot' if above 30.
"""

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        print("Please input a number.")
        return None

def interpret_weather(celsius):
    if celsius is not None:
        if celsius < 0:
            return 'Cold'
        elif 0 <= celsius <= 15:
            return 'Cool'
        elif 16 <= celsius <= 30:
            return 'Warm'
        else:
            return 'Hot'