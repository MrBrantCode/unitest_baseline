"""
QUESTION:
Write a function `rgb_to_cmyk` that takes three integers representing the red, green, and blue values of a color (ranging from 0 to 255) and returns the corresponding CMYK (Cyan, Magenta, Yellow, Key) values as a tuple of four floats, each ranging from 0 to 1. Assume the input RGB values are valid and handle the case where the input color is black.
"""

def rgb_to_cmyk(r, g, b):
    if (r == 0) and (g == 0) and (b == 0):
      # black
      return 0, 0, 0, 1

    # RGB [0,255] -> [0,1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # CMYK [0, 1]
    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k) if k != 1 else 0
    m = (1 - g - k) / (1 - k) if k != 1 else 0
    y = (1 - b - k) / (1 - k) if k != 1 else 0

    return round(c, 4), round(m, 4), round(y, 4), round(k, 4)