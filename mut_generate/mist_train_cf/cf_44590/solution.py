"""
QUESTION:
Write a function `resize_svg` that takes the width and height of the new canvas and the SVG content as input and returns the resized SVG content. The function should resize the canvas by changing the values of the width and height attributes in the SVG content, while keeping the viewBox attribute unchanged.
"""

def resize_svg(width, height, svg_content):
    """
    Resizes the SVG content by changing the values of the width and height attributes.

    Args:
        width (int): The new width of the canvas.
        height (int): The new height of the canvas.
        svg_content (str): The SVG content as a string.

    Returns:
        str: The resized SVG content.
    """

    # Find the index of the width attribute in the SVG content
    width_index = svg_content.find('width="') + 7
    # Find the index of the end of the width attribute
    width_end_index = svg_content.find('"', width_index)
    # Replace the width attribute with the new width
    svg_content = svg_content[:width_index] + str(width) + svg_content[width_end_index:]

    # Find the index of the height attribute in the SVG content
    height_index = svg_content.find('height="') + 8
    # Find the index of the end of the height attribute
    height_end_index = svg_content.find('"', height_index)
    # Replace the height attribute with the new height
    svg_content = svg_content[:height_index] + str(height) + svg_content[height_end_index:]

    return svg_content