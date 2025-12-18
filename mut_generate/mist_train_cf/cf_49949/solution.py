"""
QUESTION:
Create a function named `special_rounding` that takes a string value representing a number and two integers, `low` and `high`, representing a range. The function should return the closest integer to the input value without using built-in functions like `round()`. It should also validate that the input is a valid integer or float within the specified range. If the input is not a valid number, return "Error: Invalid input.". If the input is out of range, return "Error: Out of range.". If the number is evenly between two integers, round it towards zero. The function should handle exceptions and return appropriate error messages.
"""

def special_rounding(value, low, high):
    try:
        value = float(value)
        if value < low or value > high:
            return "Error: Out of range."
        else:
            if value >= 0:
                return int(value) if value - int(value) < 0.5 else int(value) + 1
            else:
                return int(value) if abs(value - int(value)) < 0.5 else int(value) - 1
    except ValueError:
        return "Error: Invalid input."