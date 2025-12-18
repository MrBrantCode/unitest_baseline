"""
QUESTION:
Write a function named `cmyk_to_hex(c, m, y, k)` that converts CMYK color values to their corresponding hexadecimal representation. The function should take four parameters: cyan (`c`), magenta (`m`), yellow (`y`), and key/black (`k`), all of which are floating-point numbers between 0 and 1. The function should first convert the CMYK values to RGB, then convert the RGB values to a hexadecimal string. The hexadecimal string should be in the format `#RRGGBB`, where `RR`, `GG`, and `BB` are two-digit hexadecimal numbers representing the red, green, and blue components, respectively.
"""

def cmyk_to_hex(c, m, y, k):
    r = 1.0 - min(1.0, c*(1 - k) + k)
    g = 1.0 - min(1.0, m*(1 - k) + k)
    b = 1.0 - min(1.0, y*(1 - k) + k)
    return '#{:02x}{:02x}{:02x}'.format(*tuple(int(val*255) for val in (r, g, b)))