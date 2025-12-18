"""
QUESTION:
Create a function `cmyk_to_hex(c, m, y, k)` that takes four float values in the range [0, 1] representing Cyan, Magenta, Yellow, and Key (Black) in the CMYK color model and returns the corresponding Hexadecimal (HEX) color code as a string. The function should first convert the CMYK values to RGB and then convert the RGB values to HEX.
"""

def cmyk_to_hex(c, m, y, k):
    r = round(255 * (1-c) * (1-k))
    g = round(255 * (1-m) * (1-k))
    b = round(255 * (1-y) * (1-k))
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)