"""
QUESTION:
Create a function `convert_fahrenheit_to_celsius` that takes one argument, a string representing a number in Fahrenheit. The function should convert this number to Celsius, rounded to the nearest hundredth, and return or print the result. 

The input string should be validated to ensure it represents a numeric value between -1000 and 1000, inclusive. The function should handle inputs with up to 15 decimal places and exponential notation, and should also handle inputs with leading and trailing whitespace characters. If the input is invalid, the function should print an error message and return without a result. 

The function should have a time complexity of O(1) for the conversion calculation and a space complexity of O(1) for storing variables.
"""

def convert_fahrenheit_to_celsius(fahrenheit):
    try:
        # Convert input to a float and round to 15 decimal places
        fahrenheit = round(float(fahrenheit), 15)
    except ValueError:
        print("Input is not a numeric value")
        return

    # Check if input is within the valid range
    if fahrenheit < -1000 or fahrenheit > 1000:
        print("Input is not within the valid range")
        return

    # Convert Fahrenheit to Celsius using the formula (F - 32) * 5/9
    celsius = round((fahrenheit - 32) * 5/9, 2)

    # Return the result
    return celsius