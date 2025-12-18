"""
QUESTION:
Create a function `extractCSSInfo(css)` that takes a string `css` representing the contents of a well-formatted CSS file as input. The function should return a dictionary where the keys are the CSS class names (including the dot notation) and the values are lists of tuples, each containing the property and value pairs associated with the respective class. The function should assume that each CSS class is defined using the standard dot notation and that the properties and values are listed in the standard `property: value;` format.
"""

import re

def extractCSSInfo(css):
    css_info = {}
    class_pattern = r'\.(\w+)\s*{([^}]*)}'
    property_pattern = r'(\w+)\s*:\s*([^;]+);'

    class_matches = re.finditer(class_pattern, css)
    for match in class_matches:
        class_name = "." + match.group(1)
        properties = match.group(2)
        property_matches = re.findall(property_pattern, properties)
        css_info[class_name] = property_matches

    return css_info