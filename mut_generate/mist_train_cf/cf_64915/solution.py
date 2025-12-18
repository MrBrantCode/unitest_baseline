"""
QUESTION:
Create a function `create_svg` that takes in three parameters: `size`, `color`, and `orientation`, and returns an SVG string representing a moon crescent. The SVG should have a height and width of `size`, a circle with a radius of `size/2` filled with the specified `color`, and a second circle with the same radius but filled with white and positioned to create a crescent shape. The entire SVG should be rotated by the specified `orientation` degrees around its center.
"""

def create_svg(size, color, orientation):
    svg = f"""
    <svg height="{size}" width="{size}">
        <circle cx="{size/2}" cy="{size/2}" r="{size/2}" fill={color} transform="rotate({orientation}, {size/2}, {size/2})"/>
        <circle cx="{size/2.5}" cy="{size/2}" r="{size/2}" fill="white" transform="rotate({orientation}, {size/2}, {size/2})"/>
    </svg>
    """
    return svg