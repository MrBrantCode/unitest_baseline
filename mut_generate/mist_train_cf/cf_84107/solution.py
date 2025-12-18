"""
QUESTION:
Create a function `wrap_svg_around_circle` that takes in the SVG code of an icon, the number of icons to distribute around the circle, the center coordinates (cx, cy) of the circle, and the radius (r) of the circle. The function should return the modified SVG code with the icons distributed around the circular path. 

The icons should be positioned around the circle using the formula:
`x = cx + r * cos(2π * i / n)`
`y = cy + r * sin(2π * i / n)`

Each icon should be rotated to be tangent to the circle with a rotation angle of `360 * i / n` degrees. The function should be able to handle any number of icons.
"""

import math

def wrap_svg_around_circle(icon_svg, n, cx, cy, r):
    """
    This function takes in the SVG code of an icon, the number of icons to distribute around the circle,
    the center coordinates (cx, cy) of the circle, and the radius (r) of the circle.
    
    It returns the modified SVG code with the icons distributed around the circular path.
    """
    
    # Initialize the SVG code with the circle
    svg_code = f'<svg><circle cx="{cx}" cy="{cy}" r="{r}" fill="transparent"/>'
    
    # Calculate the position and rotation for each icon
    for i in range(n):
        # Calculate the position using the formula
        x = cx + r * math.cos(2 * math.pi * i / n)
        y = cy + r * math.sin(2 * math.pi * i / n)
        
        # Calculate the rotation angle
        rotation = 360 * i / n
        
        # Add the icon to the SVG code with the calculated position and rotation
        svg_code += f'<g transform="translate({x}, {y}) rotate({rotation})">{icon_svg}</g>'
    
    # Close the SVG tag
    svg_code += '</svg>'
    
    return svg_code