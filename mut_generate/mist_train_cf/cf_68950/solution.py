"""
QUESTION:
Write a Python function named `apply_starry_night_texture` that takes an SVG string as input, applies a 'Starry Night' texture to it, and returns the resulting SVG string. The function should not rely on external graphical editors or artificial intelligence tools, and it should work directly with the SVG format.
"""

def apply_starry_night_texture(svg_string):
    """
    Applies a simplified 'Starry Night' texture to an SVG string.

    Args:
    svg_string (str): The input SVG string.

    Returns:
    str: The resulting SVG string with a simplified 'Starry Night' texture.
    """
    # This is a simplified example and actual implementation might require a more complex approach.
    # We'll just add a simple brushed texture by adding more paths with a brushed texture.
    texture = '<path d="M 10 10 L 20 20" stroke="#000" stroke-width="2" stroke-dasharray="5, 5" />'
    
    # Add the texture to the SVG string
    svg_string = svg_string.replace('</svg>', texture + '</svg>')
    
    return svg_string