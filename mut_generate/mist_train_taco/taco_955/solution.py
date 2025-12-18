"""
QUESTION:
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

Note: in `C#`, you'll always get the input as a string, so the above applies if the string isn't representing a double value.
"""

def calculate_value(value):
    try:
        # Attempt to convert the value to a float
        numeric_value = float(value)
        # Perform the calculation
        return numeric_value * 50 + 6
    except ValueError:
        # If conversion fails, return "Error"
        return 'Error'