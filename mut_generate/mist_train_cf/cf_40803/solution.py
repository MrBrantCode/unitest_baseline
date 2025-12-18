"""
QUESTION:
Implement a text formatting system with a class named `ACC` that supports the following attributes: `UNDERLINE`, `NO_UNDERLINE`, `REVERSE`, `NO_REVERSE`, and a `customrgb` method for custom RGB color attributes. Define a function `hex_to_rgb` to convert a hexadecimal color code to RGB values. The `customrgb` method should accept three arguments for red, green, and blue values. The `hex_to_rgb` function should take a hexadecimal color code as input, remove the '#' symbol if present, and return the corresponding RGB values.
"""

class ACC:
    UNDERLINE = "underline"
    NO_UNDERLINE = "no underline"
    REVERSE = "reverse"
    NO_REVERSE = "no reverse"

    @staticmethod
    def customrgb(r, g, b):
        return f"custom RGB: ({r}, {g}, {b})"

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))