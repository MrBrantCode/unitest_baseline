"""
QUESTION:
Create a function called `warp_svg` that takes an SVG string or file path, and a warping style (e.g. 'Arc', 'Bulge', 'Shell Upper', etc.) as inputs and returns the warped SVG string.
"""

import xml.etree.ElementTree as ET

def warp_svg(svg_string, warping_style):
    """
    Warp an SVG string using a specified warping style.

    Args:
    svg_string (str): The SVG string to be warped.
    warping_style (str): The style to use for warping (e.g. 'Arc', 'Bulge', 'Shell Upper', etc.)

    Returns:
    str: The warped SVG string.
    """

    # Parse the SVG string into an ElementTree object
    root = ET.fromstring(svg_string)

    # TO DO: Implement the warping logic based on the warping style
    # This will likely involve manipulating the underlying XML structure of the SVG file
    # For example, you might need to adjust the 'd' attribute of path elements

    # Return the warped SVG string
    return ET.tostring(root, encoding='unicode')