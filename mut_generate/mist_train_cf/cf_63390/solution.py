"""
QUESTION:
Function: break_svg_into_parts

Given an SVG file containing multiple parts, break it down into individual parts and save each part as a separate SVG file.

Restriction: The input SVG file should be in a format that can be edited using a web-based SVG editor like SVG-edit.
"""

import re

def break_svg_into_parts(svg_string):
    """
    Breaks an SVG string into individual parts and saves each part as a separate SVG file.
    
    Args:
        svg_string (str): The input SVG string.
    
    Returns:
        list: A list of SVG strings, each representing a separate part.
    """

    # Assuming each part in the SVG string is enclosed in a 'g' tag
    pattern = r'<g[^>]*>(.*?)</g>'
    
    # Use regular expression to find all 'g' tags and their contents
    parts = re.findall(pattern, svg_string, re.DOTALL)
    
    # Initialize an empty list to store the individual SVG parts
    svg_parts = []
    
    # Iterate over each part
    for i, part in enumerate(parts):
        # Create a new SVG string for the current part
        svg_part = '<svg>' + part + '</svg>'
        
        # Add the new SVG string to the list
        svg_parts.append(svg_part)
    
    return svg_parts