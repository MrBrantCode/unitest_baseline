"""
QUESTION:
Implement a function `special_rounding` that accepts a string representing a number, two integers `low` and `high` as range limits, and a list of integers `exclude`. The function should return the integer closest to the input value without using built-in functions like `round()`. It should check if the given value is a valid integer or floating point number and if it falls within the specified range. If not, return an error message. When the number is equidistant from both integers, round it off to the one closer to zero. If the closest integer is in the exclude list, return an error message.
"""

def special_rounding(value, low, high, exclude):
    """
    This function rounds a given number to the closest integer without using built-in functions like round().
    It checks if the number is a valid integer or floating point number and if it falls within the specified range.
    If the number is equidistant from both integers, it rounds off to the one closer to zero.
    If the closest integer is in the exclude list, it returns an error message.

    Parameters:
    value (str): A string representing a number.
    low (int): The lower limit of the range.
    high (int): The upper limit of the range.
    exclude (list): A list of integers to exclude.

    Returns:
    int or str: The closest integer to the input value, or an error message if the input is invalid or out of range.
    """

    try:
        number = float(value)
    except ValueError:
        return "Error: Invalid input."

    if number < low or number > high:
        return "Error: Out of range."

    floor_val = int(number)
    ceil_val = floor_val if number == floor_val else floor_val + 1
    closest = floor_val if abs(floor_val - number) < abs(ceil_val - number) else ceil_val

    if closest in exclude:
        return "Error: Number is in the exclude list."
    else:
        return closest