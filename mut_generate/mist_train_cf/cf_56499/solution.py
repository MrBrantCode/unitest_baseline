"""
QUESTION:
Write a function named `volume` that calculates the volume of a trapezoidal prism given its length, height, top width, and bottom width. The function should return the calculated volume. The formula for the volume is the area of the trapezoidal base times the length, where the area of the trapezoidal base is calculated as half the sum of the top and bottom widths times the height.
"""

def trapezoidal_prism_volume(length, height, top_width, bottom_width):
    """
    Calculate the volume of a trapezoidal prism given its length, height, top width, and bottom width.

    Args:
    length (float): Length of the prism.
    height (float): Height of the prism.
    top_width (float): Top width of the prism.
    bottom_width (float): Bottom width of the prism.

    Returns:
    float: Calculated volume of the trapezoidal prism.
    """
    area = (1/2) * (top_width + bottom_width) * height
    return area * length