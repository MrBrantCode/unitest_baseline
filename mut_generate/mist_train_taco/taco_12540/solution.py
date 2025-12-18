"""
QUESTION:
We all use 16:9, 16:10, 4:3 etc. ratios every day. Main task is to determine image ratio by its width and height dimensions. 

Function should take width and height of an image and return a ratio string (ex."16:9").
If any of width or height entry is 0 function should throw an exception (or return `Nothing`).
"""

from fractions import Fraction

def calculate_image_ratio(width: int, height: int) -> str:
    """
    Calculate the ratio of an image based on its width and height.

    Parameters:
    - width (int): The width of the image.
    - height (int): The height of the image.

    Returns:
    - str: The ratio of the image in the format "numerator:denominator".

    Raises:
    - ValueError: If either width or height is 0.
    """
    if width == 0 or height == 0:
        raise ValueError("Width and height must be non-zero values.")
    
    ratio = Fraction(width, height)
    return f"{ratio.numerator}:{ratio.denominator}"