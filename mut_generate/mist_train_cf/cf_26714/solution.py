"""
QUESTION:
Write a function `extractCSSInfo(css)` that takes a string `css` representing the contents of a well-formed CSS file as input, where each class is defined as a block of CSS properties enclosed within curly braces `{}` and preceded by a period `.`, and each property is represented as a key-value pair within the class block. The function should parse the CSS content and return a dictionary mapping each CSS class to its properties.
"""

import re

def extractCSSInfo(css):
    css_info = {}
    class_pattern = r'\.([\w-]+)\s*{([^}]*)}'
    property_pattern = r'(\w+)\s*:\s*([^;]+);'

    class_matches = re.finditer(class_pattern, css)
    for match in class_matches:
        class_name = match.group(1)
        properties = match.group(2)
        property_matches = re.finditer(property_pattern, properties)
        class_properties = {}
        for prop_match in property_matches:
            class_properties[prop_match.group(1)] = prop_match.group(2).strip()
        css_info[class_name] = class_properties

    return css_info