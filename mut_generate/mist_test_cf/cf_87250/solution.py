"""
QUESTION:
Create a function named `rgb_to_hex` that takes a single argument `rgb`. The function should convert the given RGB value to a HEX color code and return the result as a string. The `rgb` argument can be an integer, float, string, or tuple, representing the red, green, and blue components of the RGB value.

If `rgb` is an integer, float, or string, it will be treated as a single value and applied to all three components. If `rgb` is a tuple, it should contain exactly three values for the red, green, and blue components. The values can be integers, floats, hexadecimal strings, binary strings, octal strings, or scientific notation strings.

The function should handle invalid RGB values, where any of the three components is negative or greater than 255. In such cases, the function should return "Invalid RGB value". The function should also handle invalid input types and return "Invalid input type" if the input is not of type integer, float, string, or tuple.

The function should return the HEX color code as a string, prefixed with "#". If a hexadecimal value for a component is a single digit, it should be prepended with a zero.
"""

def rgb_to_hex(rgb):
    if not isinstance(rgb, (int, float, str, tuple)):
        return "Invalid input type"
    
    if isinstance(rgb, str):
        try:
            rgb = int(rgb)
        except ValueError:
            return "Invalid input type"
    
    if isinstance(rgb, (int, float)):
        rgb = round(float(rgb))
        if rgb < 0 or rgb > 255:
            return "Invalid RGB value"
        rgb = (rgb, rgb, rgb)
    
    if isinstance(rgb, tuple):
        if len(rgb) != 3:
            return "Invalid RGB value"
        r, g, b = rgb
        if not (isinstance(r, (int, float)) and isinstance(g, (int, float)) and isinstance(b, (int, float))):
            return "Invalid input type"
        r = round(float(r))
        g = round(float(g))
        b = round(float(b))
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return "Invalid RGB value"
        rgb = (r, g, b)
    
    hex_r = hex(rgb[0])[2:].zfill(2)
    hex_g = hex(rgb[1])[2:].zfill(2)
    hex_b = hex(rgb[2])[2:].zfill(2)
    
    return "#" + hex_r + hex_g + hex_b