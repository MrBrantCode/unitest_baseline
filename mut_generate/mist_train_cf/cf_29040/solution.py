"""
QUESTION:
Write a function `toHex` that takes a list of three integers (0 <= value <= 255) representing the RGB color and returns a string representing the hexadecimal color code in the format "#rrggbb", where rr, gg, and bb are two-digit hexadecimal representations of the red, green, and blue values respectively.
"""

from typing import List

def toHex(rgb: List[int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])