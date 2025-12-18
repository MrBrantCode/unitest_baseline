"""
QUESTION:
Write a function named resize_svg() to resize an SVG image. The function should take the width, height, viewBox, and the SVG path 'd' attribute as input, and return the resized SVG image as a string. The resized SVG image should have the same viewBox but with the width and height changed to the specified values. The function should not modify the SVG path 'd' attribute. The width and height can be different from the original size.
"""

def resize_svg(width, height, viewBox, path_d):
    """
    Resize an SVG image by changing its width and height while keeping the viewBox the same.

    Args:
    width (int): The new width of the SVG image.
    height (int): The new height of the SVG image.
    viewBox (str): The viewBox of the SVG image.
    path_d (str): The 'd' attribute of the SVG path.

    Returns:
    str: The resized SVG image as a string.
    """
    return f'<svg width="{width}" height="{height}" viewBox="{viewBox}" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="{path_d}" fill="#212121"/></svg>'