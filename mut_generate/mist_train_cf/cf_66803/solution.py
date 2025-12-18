"""
QUESTION:
Write a function called `distort_svg` that takes as input an SVG path and returns a distorted or warped version of the SVG path. The function should apply transformations to the points in the SVG path to achieve the distortion. Please provide a description of the type of distortion the function should apply (e.g. stretching, compressing, rotating, etc.). The function should not rely on external libraries or software, and should implement the distortion algorithm programmatically.
"""

import re

def distort_svg(svg_path, scale_x=1, scale_y=1):
    """
    Applies a scaling transformation to the points in the SVG path.

    Args:
        svg_path (str): The SVG path to be distorted.
        scale_x (float): The scaling factor for the x-axis.
        scale_y (float): The scaling factor for the y-axis.

    Returns:
        str: The distorted SVG path.
    """

    # Use regular expression to find all the coordinates in the SVG path
    coords = re.findall(r'(\d+(\.\d+)?),(\d+(\.\d+)?)', svg_path)

    # Apply the scaling transformation to each coordinate
    distorted_coords = []
    for x, _, y, _ in coords:
        distorted_x = str(float(x) * scale_x)
        distorted_y = str(float(y) * scale_y)
        distorted_coords.append(f"{distorted_x},{distorted_y}")

    # Replace the original coordinates with the distorted coordinates
    distorted_path = re.sub(r'(\d+(\.\d+)?),(\d+(\.\d+)?)', lambda match: distorted_coords.pop(0), svg_path)

    return distorted_path