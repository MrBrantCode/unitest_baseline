"""
QUESTION:
Write a function `hex_to_rgb(hex_code)` that takes a string `hex_code` representing a hexadecimal color code and returns the RGB equivalent of the color if it is non-transparent, or a message indicating that the color is transparent, or an error message if the input is not a valid hexadecimal color code. A valid hexadecimal color code starts with a '#' and is followed by 6 or 3 alphanumeric characters. The function should also handle the case where the input is a valid hexadecimal color code but represents a transparent color (i.e., "#000000").
"""

import re

def hex_to_rgb(hex_code):
    # Check if color code is non-transparent
    if hex_code != "#000000":
        # Using search() method of re module
        match = re.search("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", hex_code)
        if match:
            hex_code = hex_code.lstrip('#')
            # If the hex_code length is 3, convert to 6 character hex_code
            if len(hex_code) == 3:
                hex_code = ''.join([c*2 for c in hex_code])
            rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
            return rgb
        else:
            return "Invalid Hex Code"
    else:
        return "This color code represents transparent color"