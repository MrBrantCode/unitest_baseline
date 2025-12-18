"""
QUESTION:
Implement a function `count_css_properties` that takes a CSS code snippet as a string and returns a dictionary mapping each unique CSS property to its occurrence count. The CSS code snippet is a string where each property is defined as a key-value pair. The function should only consider the property name before the colon and ignore any code blocks or nested properties.
"""

def count_css_properties(css_code: str) -> dict:
    properties = {}
    lines = css_code.split('\n')
    for line in lines:
        if ':' in line:
            property_name = line.split(':')[0].strip()
            if property_name in properties:
                properties[property_name] += 1
            else:
                properties[property_name] = 1
    return properties