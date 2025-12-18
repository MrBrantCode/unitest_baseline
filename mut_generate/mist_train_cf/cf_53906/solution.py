"""
QUESTION:
Develop a function `cmyk_to_hex` that takes four CMYK color values (cyan, magenta, yellow, key) as input, each ranging from 0 to 1, and returns the corresponding HEX color representation as a string. The conversion should be based on the formula: RGB = 255 * (1 - CMYK) * (1 - K), where the result is rounded to the nearest whole number.
"""

def cmyk_to_hex(c, m, y, k):
    r = round(255 * (1.0 - c) * (1.0 - k))
    g = round(255 * (1.0 - m) * (1.0 - k))
    b = round(255 * (1.0 - y) * (1.0 - k))
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)