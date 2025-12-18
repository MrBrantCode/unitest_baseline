"""
QUESTION:
Create a function named `create_svg_circle()` that takes user input for the radius and color of a circle, as well as its x and y position on a 500x500 SVG canvas. The function should return a string representing the SVG code to draw the circle with the given properties. The circle's x and y position should be specified by the user, but the canvas dimensions are fixed at 500x500.
"""

def create_svg_circle(radius, color, position_x, position_y):
    svg_code = f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500">\n'
    svg_code += f'\t<circle cx="{position_x}" cy="{position_y}" r="{radius}" fill="{color}" />\n'
    svg_code += '</svg>'

    return svg_code