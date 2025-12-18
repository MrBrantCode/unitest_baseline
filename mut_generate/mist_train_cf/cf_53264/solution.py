"""
QUESTION:
Create a function named `cmyk_to_hex` that converts CMYK color values to their corresponding HEX representation. The function should take four parameters: cyan (c), magenta (m), yellow (y), and key (black) (k) coefficients, which are floating point numbers between 0 and 1. The function should return a string representing the HEX color value.
"""

def cmyk_to_hex(c, m, y, k):
    """
    This function converts CMYK color values to their corresponding HEX representation.
    
    Parameters:
    c (float): Cyan coefficient between 0 and 1.
    m (float): Magenta coefficient between 0 and 1.
    y (float): Yellow coefficient between 0 and 1.
    k (float): Key (black) coefficient between 0 and 1.
    
    Returns:
    str: A string representing the HEX color value.
    """
    r = 255 * (1-c) * (1-k)
    g = 255 * (1-m) * (1-k)
    b = 255 * (1-y) * (1-k)
    return '#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b))