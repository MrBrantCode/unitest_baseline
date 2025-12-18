"""
QUESTION:
Create a function `convertRGBtoHEX` that takes an RGB value as input, which is a tuple of three integers representing red, green, and blue color values in the range of 0 to 255. The function should return a string representing the equivalent HEX value. If the input RGB value is invalid, the function should return "000000".
"""

def convertRGBtoHEX(rgb):
    """
    Convert an RGB value to its equivalent HEX value.

    Args:
        rgb (tuple): A tuple of three integers representing red, green, and blue color values in the range of 0 to 255.

    Returns:
        str: A string representing the equivalent HEX value. If the input RGB value is invalid, returns "000000".
    """
    if not isinstance(rgb, tuple) or len(rgb) != 3 or not all(0 <= val <= 255 for val in rgb):
        return "000000"
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])