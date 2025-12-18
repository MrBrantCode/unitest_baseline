"""
QUESTION:
Write a function `check_and_convert(hex_color)` that checks if a given string input is a valid hexadecimal color code and converts it into its RGB equivalent. The function should be able to handle both shorthand (3-digit) and full form (6-digit) hexadecimal color codes, and return the RGB value as a tuple if the input is valid, or the string "Invalid hexadecimal color code" if it's not. The input string may or may not start with '#'.
"""

import re

def check_and_convert(hex_color):
    # Remove "#" if it exists at the beginning of the hex_color string
    if hex_color[0] == '#':
        hex_color = hex_color[1:]
    # Define the regular expression for hexadecimal color
    hex_color_pattern = r'^([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$'
    # Validate the given string input
    if re.match(hex_color_pattern, hex_color):
        # If the color is in short form, double each digit
        if len(hex_color) == 3:
            hex_color = ''.join([ch * 2 for ch in hex_color])
        # Convert the hex color to RGB
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    else:
        return "Invalid hexadecimal color code"