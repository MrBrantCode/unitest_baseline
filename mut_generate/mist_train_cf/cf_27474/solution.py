"""
QUESTION:
Create a function `parseCSS` that takes a string `cssCode` as input and returns a dictionary. The dictionary should have CSS selectors as keys and lists of their corresponding properties as values. The CSS selectors and properties are separated by curly braces `{}` in the input string. Each property should be in the format `property: value`. The function should assume that the input CSS code is well-formed and valid.
"""

import re

def parseCSS(cssCode):
    css_dict = {}
    selector_pattern = r'([^\{\}]+)\s*\{([^\{\}]+)\}'
    property_pattern = r'([^:]+):([^;]+);'

    matches = re.finditer(selector_pattern, cssCode)
    for match in matches:
        selector = match.group(1).strip()
        properties = match.group(2).strip()
        property_matches = re.finditer(property_pattern, properties)
        property_list = [f'{prop.group(1).strip()}: {prop.group(2).strip()}' for prop in property_matches]
        css_dict[selector] = property_list

    return css_dict