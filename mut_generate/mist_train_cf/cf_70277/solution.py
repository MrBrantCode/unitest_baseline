"""
QUESTION:
Create a function named `wrap_svg_in_circle` that places an SVG within a circular path. The function should take in the SVG string, the radius of the circular path, the x-coordinate of the center of the circular path (cx), and the y-coordinate of the center of the circular path (cy). The function should return the modified SVG string with the SVG placed within the circular path. Note that this function will not actually wrap the SVG around the circular path, but rather encase it within the circle.
"""

def wrap_svg_in_circle(svg_string, radius, cx, cy):
    # Encase the SVG within a circle by adding a circle element with the necessary radius, cx, and cy attributes
    circle_element = f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="black" />'
    # Create a new SVG string with the circle element and the original SVG
    new_svg_string = f'<svg width="{2*radius}" height="{2*radius}">{circle_element}{svg_string}</svg>'
    return new_svg_string