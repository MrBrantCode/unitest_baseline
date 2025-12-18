"""
QUESTION:
Create a function `convert_to_fahrenheit(celsius)` that takes a real number `celsius` as input and returns its equivalent temperature in Fahrenheit as an integer. The function should check if `celsius` is within the valid range of -273.15 to 1000, and if not, return an error message "Invalid input temperature".
"""

def convert_to_fahrenheit(celsius):
    # Check if the input temperature is within a valid range
    if celsius < -273.15 or celsius > 1000:
        return "Invalid input temperature"

    # Conversion formula
    fahrenheit = round(celsius * 9/5 + 32)

    return fahrenheit