"""
QUESTION:
Implement a function `colour_to_hex(rgb: Tuple[int, int, int]) -> str` that takes a tuple of three integers representing the red, green, and blue components of a color and returns a string representing the hexadecimal color code. The function should ensure that each component value is between 0 and 255, inclusive. The output string should be in the format `#RRGGBB`, where `RR`, `GG`, and `BB` are two-digit hexadecimal representations of the red, green, and blue components, respectively.
"""

from typing import Tuple

def colour_to_hex(rgb: Tuple[int, int, int]) -> str:
    # Convert each RGB component to its corresponding hexadecimal representation
    hex_code = "#{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])
    return hex_code