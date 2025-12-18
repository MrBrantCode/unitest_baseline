"""
QUESTION:
Morph an SVG shape into another shape by transitioning from one 'd' attribute to another using the SVG's animate tag. Create a function `morph_svg` that takes the original SVG path and the target SVG path as input and returns the animated SVG code. 

Restrictions: The number of command points in both the original and target shapes should be the same for a successful morphing.
"""

def morph_svg(original_path, target_path):
    """
    This function morphs an SVG shape into another shape by transitioning 
    from one 'd' attribute to another using the SVG's animate tag.

    Args:
        original_path (str): The original SVG path.
        target_path (str): The target SVG path.

    Returns:
        str: The animated SVG code.
    """

    # Create the SVG path with the original path and the animation tag
    svg_code = f'<svg> <path d="{original_path}" id="firstShape">'
    svg_code += f'<animate attributeName="d" begin="mouseover" dur="1s" repeatCount="indefinite"'
    svg_code += f'from="{original_path}" to="{target_path}" />'
    svg_code += '</path></svg>'

    return svg_code