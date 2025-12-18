"""
QUESTION:
Write a Python function named `break_down_svg` that takes a string representing an SVG document as input and returns a list of dictionaries, where each dictionary represents a 'path' element in the SVG and contains its attributes.

The function should be able to handle multiple 'path' elements in the SVG and should include the SVG namespace when finding the 'path' elements. 

The function should be able to extract the 'd' and 'fill' attributes of each 'path' element. 

Note that the function will only extract 'path' elements and not other elements like 'circle', 'rect', etc. Also, it will not break down complex SVG paths into individual parts.
"""

import xml.etree.ElementTree as ET

def break_down_svg(svg_data):
    """
    Breaks down an SVG document into its 'path' elements.
    
    Args:
        svg_data (str): A string representing an SVG document.
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a 'path' element in the SVG and contains its attributes.
    """
    root = ET.fromstring(svg_data)
    paths = root.findall('.//{http://www.w3.org/2000/svg}path')
    return [path.attrib for path in paths]