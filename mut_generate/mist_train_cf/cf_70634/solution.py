"""
QUESTION:
Create a function named `add_magic_to_svg` that takes in a string representing the SVG code of a key and returns a new SVG string with a touch of whimsy and magic. The function should only modify the SVG code to add a magical glow to the key using a filter, and not add any surrounding elements or change the overall structure of the SVG.
"""

def add_magic_to_svg(svg_code):
    """
    Adds a magical glow to an SVG image using a filter.

    Args:
    svg_code (str): The SVG code of the image.

    Returns:
    str: The modified SVG code with a magical glow.
    """

    # Add a filter to create a magical glow effect
    glow_filter = '<filter id="magic-glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" /><feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 19 -9" result="glow" /><feComposite in="SourceGraphic" in2="glow" operator="arithmetic" k2="1" k3="1" result="lit" /></filter>'

    # Add the filter to the SVG code
    modified_svg_code = svg_code.replace('<svg', '<svg>' + glow_filter)

    # Apply the filter to all elements in the SVG
    modified_svg_code = modified_svg_code.replace('<path', '<path filter="url(#magic-glow)"')
    modified_svg_code = modified_svg_code.replace('<rect', '<rect filter="url(#magic-glow)"')
    modified_svg_code = modified_svg_code.replace('<circle', '<circle filter="url(#magic-glow)"')
    modified_svg_code = modified_svg_code.replace('<ellipse', '<ellipse filter="url(#magic-glow)"')
    modified_svg_code = modified_svg_code.replace('<polygon', '<polygon filter="url(#magic-glow)"')
    modified_svg_code = modified_svg_code.replace('<line', '<line filter="url(#magic-glow)"')

    return modified_svg_code