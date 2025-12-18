"""
QUESTION:
Create a function named `cmyk_to_hex` that converts CMYK color values to their equivalent hexadecimal color code. The function should take four parameters: c, m, y, and k, representing Cyan, Magenta, Yellow, and Key/Black values respectively. The CMYK values are between 0 and 1. The function should return a string representing the hexadecimal color code.
"""

def cmyk_to_hex(c, m, y, k):
    """
    Converts CMYK color values to their equivalent hexadecimal color code.

    Args:
        c (float): Cyan value between 0 and 1.
        m (float): Magenta value between 0 and 1.
        y (float): Yellow value between 0 and 1.
        k (float): Key/Black value between 0 and 1.

    Returns:
        str: A string representing the hexadecimal color code.
    """
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return '#%02x%02x%02x' % (round(r), round(g), round(b))