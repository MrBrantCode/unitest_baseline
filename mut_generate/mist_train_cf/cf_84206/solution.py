"""
QUESTION:
Create a function `cmyk_to_hex` that takes four arguments: `c`, `m`, `y`, and `k`, representing the cyan, magenta, yellow, and black components of a CMYK color, respectively, all in the range of 0 to 1. The function should return the equivalent hexadecimal color code. Note that the output may not exactly match the original CMYK color due to differences in color rendering, and the implementation should round the intermediate RGB values to the nearest whole number.
"""

def cmyk_to_hex(c, m, y, k):
    """
    Converts CMYK color to its equivalent hexadecimal color code.
    
    Args:
        c (float): The cyan component of the CMYK color, in the range of 0 to 1.
        m (float): The magenta component of the CMYK color, in the range of 0 to 1.
        y (float): The yellow component of the CMYK color, in the range of 0 to 1.
        k (float): The black component of the CMYK color, in the range of 0 to 1.
    
    Returns:
        str: The equivalent hexadecimal color code.
    """
    r = round(255 * (1-c) * (1-k))
    g = round(255 * (1-m) * (1-k))
    b = round(255 * (1-y) * (1-k))
    return "#{:02x}{:02x}{:02x}".format(r, g, b)