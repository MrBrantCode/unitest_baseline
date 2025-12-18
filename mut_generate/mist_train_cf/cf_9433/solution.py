"""
QUESTION:
Create a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature value as input and returns its Celsius equivalent. The function should handle decimal values, round the Celsius result to the nearest tenth, and return an error message for non-numeric input or temperatures outside the valid range of -459.67°F to 1000°F.
"""

def fahrenheit_to_celsius(fahrenheit):
    try:
        # Convert the input to a float
        fahrenheit = float(fahrenheit)
    except ValueError:
        return "Invalid input. Please enter a numeric value."
    
    if fahrenheit < -459.67 or fahrenheit > 1000:
        return "Invalid temperature value. Please enter a value between -459.67°F and 1000°F."
    
    # Calculate the Celsius value
    celsius = (fahrenheit - 32) * 5/9
    # Round to the nearest tenth
    celsius = round(celsius, 1)
    
    return celsius