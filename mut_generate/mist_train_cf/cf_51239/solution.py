"""
QUESTION:
Write a function `get_color` that takes a bar number (1-12) as input and returns the corresponding color of the bar in the SVG file. The colors are: `#f9f9f9`, `#ff0`, `#0ff`, `#0f0`, `#f0f`, `red`, `#00f`, and `#090909`.
"""

def get_color(bar_number):
    """
    This function returns the corresponding color of the bar in the SVG file.
    
    Parameters:
    bar_number (int): The bar number (1-12)
    
    Returns:
    str: The color of the bar
    """
    colors = ["#f9f9f9", "#ff0", "#0ff", "#0f0", "#f0f", "red", "#00f", "#090909"]
    if 1 <= bar_number <= 12:
        return colors[(bar_number - 1) % len(colors)]
    else:
        return "Invalid bar number"