"""
QUESTION:
Create a function that applies a blur effect to an SVG image. The function should take the SVG image as a string and return the blurred SVG image as a string.
"""

def blur_svg(svg_string, blur_radius):
    """
    Applies a blur effect to an SVG image.

    Args:
    svg_string (str): The SVG image as a string.
    blur_radius (int): The radius of the blur effect.

    Returns:
    str: The blurred SVG image as a string.
    """
    return svg_string.replace("<svg", f"<svg style='filter: blur({blur_radius}px);'")