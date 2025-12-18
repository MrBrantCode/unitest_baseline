"""
QUESTION:
Create a function `parseSVGAttributes(svgCode: str) -> dict` that takes a string `svgCode` representing a well-formed SVG code snippet as input and returns a dictionary containing the extracted attribute-value pairs for the following attributes: `stroke-linejoin`, `xmlns`, `height`, `viewBox`, `width`, and `path`. The function should handle the presence and absence of attributes gracefully, excluding non-existent attributes from the output dictionary.
"""

import re

def entrance(svgCode: str) -> dict:
    attributes = ["stroke-linejoin", "xmlns", "height", "viewBox", "width", "path"]
    attribute_values = {}
    
    for attribute in attributes:
        match = re.search(fr'{attribute}="([^"]+)"', svgCode)
        if match:
            attribute_values[attribute] = match.group(1)
    
    return attribute_values