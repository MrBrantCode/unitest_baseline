"""
QUESTION:
Create an SVG element with semi-transparent parts using the `fill-opacity` attribute. The element is a path with a given color and the desired level of transparency is 50%.
"""

def generate_svg_element(color, opacity):
    """
    Generate an SVG path element with a given color and transparency level.

    Args:
    color (str): The color of the path element.
    opacity (float): The level of transparency, ranging from 0.0 to 1.0.

    Returns:
    str: The SVG path element as a string.
    """
    return f'<path fill-rule="evenodd" clip-rule="evenodd" d="M1.15625 8.59375C1....Z" fill="{color}" fill-opacity="{opacity}"/>'

# Generate an SVG path element with a color and 50% opacity
svg_element = generate_svg_element("#212121", 0.5)
print(svg_element)