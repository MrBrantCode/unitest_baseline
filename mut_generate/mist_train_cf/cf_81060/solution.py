"""
QUESTION:
The function is to modify an SVG image to make it responsive to different screen sizes. The given SVG has a fixed width and height of 32 units. The task is to modify the SVG so that it can adapt to various screen sizes without losing its aspect ratio. The modification should be done in such a way that the aspect ratio remains the same, and the SVG can be scaled up or down based on the available space.
"""

def make_svg_responsive(svg_string):
    """
    Modify an SVG image to make it responsive to different screen sizes.

    Args:
    svg_string (str): The input SVG string.

    Returns:
    str: The modified SVG string with width and height set to 100%.
    """
    svg_lines = svg_string.splitlines()
    for i, line in enumerate(svg_lines):
        if line.startswith('<svg'):
            svg_lines[i] = line.replace('width="32"', 'width="100%"').replace('height="32"', 'height="100%"')
    return '\n'.join(svg_lines)