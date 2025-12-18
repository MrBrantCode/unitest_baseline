"""
QUESTION:
Create a function called `add_car_color` that takes in a JSON object and a color value, and adds a new field "car color" to the JSON object with the given color value. The color value can be in RGB format (e.g., (255, 0, 0)), hexadecimal format (e.g., #FF0000), or a color name (e.g., red, blue, green). If the color value is not valid according to the RGB color model, raise a custom exception called `InvalidColorException` with an appropriate error message.
"""

import re

class InvalidColorException(Exception):
    pass

def add_car_color(json_obj, color):
    """
    Adds a new field "car color" to the JSON object with the given color value.

    Args:
    json_obj (dict): The JSON object to modify.
    color (str): The color value in RGB format (e.g., (255, 0, 0)), hexadecimal format (e.g., #FF0000), or a color name (e.g., red, blue, green).

    Raises:
    InvalidColorException: If the color value is not valid according to the RGB color model.

    Returns:
    dict: The modified JSON object with the added "car color" field.
    """
    # Check if the color is in RGB format
    if re.match(r'\(\d{1,3}, \d{1,3}, \d{1,3}\)', color):
        rgb_values = re.findall(r'\d{1,3}', color)
        # Check if each RGB value is between 0 and 255
        if all(0 <= int(value) <= 255 for value in rgb_values):
            json_obj['car color'] = color
        else:
            raise InvalidColorException(f"{color} is not a valid color.")
    # Check if the color is in hexadecimal format
    elif re.match(r'#[a-fA-F0-9]{6}', color):
        json_obj['car color'] = color
    # Check if the color is a known color name
    elif re.match(r'[a-zA-Z]+', color):
        json_obj['car color'] = color
    else:
        raise InvalidColorException(f"{color} is not a valid color.")

    return json_obj