"""
QUESTION:
Create a function `fahrenheit_to_celsius(fahrenheit)` that takes a temperature value in Fahrenheit as input and returns the equivalent temperature value in Celsius, rounded to the nearest tenth. The function should handle invalid inputs, including non-numeric values and temperatures outside the valid range of -459.67°F to 1000°F, and return an error message in such cases.
"""

def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        return "Invalid input. Please enter a numeric value."
    
    if fahrenheit < -459.67 or fahrenheit > 1000:
        return "Invalid temperature value. Please enter a value between -459.67°F and 1000°F."
    
    celsius = (fahrenheit - 32) * 5/9
    celsius = round(celsius, 1)
    
    return celsius