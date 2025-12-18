"""
QUESTION:
Write a function `rgb_to_cmyk` that takes three RGB color values as input, ranging from 0 to 255, and returns the corresponding CMYK color values as a tuple of four values, each ranging from 0% to 100%. The conversion formulas are as follows:

C = (1 - R/255 - K) / (1 - K) * 100
M = (1 - G/255 - K) / (1 - K) * 100
Y = (1 - B/255 - K) / (1 - K) * 100
K = 1 - max(R/255, G/255, B/255)

The function should return the CMYK values with a precision of one decimal place.
"""

def rgb_to_cmyk(R, G, B):
    """
    Convert RGB color values to CMYK color values.

    Args:
    R (int): Red color value, ranging from 0 to 255.
    G (int): Green color value, ranging from 0 to 255.
    B (int): Blue color value, ranging from 0 to 255.

    Returns:
    tuple: A tuple containing the CMYK color values, each ranging from 0% to 100%.
    """

    # Normalize RGB values to the range 0-1
    R, G, B = R / 255.0, G / 255.0, B / 255.0

    # Calculate CMYK color values
    K = 1 - max(R, G, B)
    C = round((1 - R - K) / (1 - K) * 100, 1) if (1 - K) != 0 else 0
    M = round((1 - G - K) / (1 - K) * 100, 1) if (1 - K) != 0 else 0
    Y = round((1 - B - K) / (1 - K) * 100, 1) if (1 - K) != 0 else 0
    K = round(K * 100, 1)

    return (C, M, Y, K)