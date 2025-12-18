"""
QUESTION:
Create a function `add_gradient_fill` that takes an SVG path and returns the SVG with a linear gradient fill applied. The gradient should be from red at the top left to blue at the bottom right. The function should return the modified SVG as a string. The input path should be a string and the function should be able to handle any valid SVG path.
"""

def add_gradient_fill(path):
    """
    This function takes an SVG path and returns the SVG with a linear gradient fill applied.
    The gradient is from red at the top left to blue at the bottom right.

    Args:
        path (str): A valid SVG path.

    Returns:
        str: The modified SVG as a string.
    """
    svg = "<svg width='32' height='32' viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'>"
    svg += "<defs><linearGradient id='gradient' x1='0%' y1='0%' x2='100%' y2='100%'>"
    svg += "<stop offset='0%' stop-color='#FF0000'/><stop offset='100%' stop-color='#0000FF'/>"
    svg += "</linearGradient></defs><path d='" + path + "' fill='url(#gradient)'/>"
    svg += "</svg>"
    return svg