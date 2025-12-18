"""
QUESTION:
Write a function `extractSelectorsAndProperties(css)` that takes a string `css` representing the content of a CSS file as input, where the CSS content is well-formed, does not contain syntax errors, and may include classes, IDs, and nested selectors. The function should return a dictionary where the keys are the selectors and the values are lists of properties associated with each selector, with properties represented as strings in the format "property: value".
"""

import re

def extractSelectorsAndProperties(css):
    selector_property_dict = {}
    selector = ""
    properties = []

    lines = css.split("\n")
    for line in lines:
        line = line.strip()
        if line and not line.startswith("//") and not line.startswith("/*"):
            if line.endswith("{"):
                selector = line[:-1].strip()
                properties = []
            elif line.endswith("}"):
                selector_property_dict[selector] = properties
            else:
                property_match = re.match(r'\s*([^:]+)\s*:\s*([^;]+)\s*;', line)
                if property_match:
                    property = f"{property_match.group(1)}: {property_match.group(2)}"
                    properties.append(property)

    return selector_property_dict