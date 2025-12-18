"""
QUESTION:
Write a function `add_tooltip` that adds an interactive tooltip to an SVG element using the "title" tag. The function should take an SVG path and a tooltip text as input, and return the modified SVG path with the added tooltip. Note that the solution should not rely on any external libraries or CSS, and should be compatible with standard SVG rendering.
"""

def add_tooltip(svg_path, tooltip_text):
    return f'<title>{tooltip_text}</title>{svg_path}'