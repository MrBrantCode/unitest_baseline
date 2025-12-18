"""
QUESTION:
Write a function `decode_hex_color_with_error_checking` that takes a string of space-separated color codes in an unusual hexadecimal composition (e.g., '#fff', '#000', '#f00') and integers. The function should return a list of tuples, each containing RGB values corresponding to the input color codes. If any invalid color code is encountered, the function should return "Error: Invalid Input". The color codes '#fff', '#000', '#f00', '#0f0', '#00f', '#ff0', '#0ff', '#f0f' should be supported, representing white, black, red, green, blue, yellow, cyan, and magenta, respectively.
"""

from typing import Union, List, Tuple

def decode_hex_color_with_error_checking(color_string: str) -> Union[List[Tuple[int, int, int]], str]:
    color_string_list = color_string.split(' ')
    hex_codes = {
        '#fff': (255, 255, 255),
        '#000': (0, 0, 0),
        '#f00': (255, 0, 0),
        '#0f0': (0, 255, 0),
        '#00f': (0, 0, 255),
        '#ff0': (255, 255, 0),
        '#0ff': (0, 255, 255),
        '#f0f': (255, 0, 255),
    }
    try:
        rgb_values = [hex_codes[color] for color in color_string_list]
        return rgb_values
    except KeyError:  # color code not in hexadecimal codes dict
        return "Error: Invalid Input"