"""
QUESTION:
Implement a function `parse_html_attributes(html: str) -> dict` that takes a string `html` representing the HTML code as input, parses it, and returns a dictionary where the keys are the HTML element names and the values are dictionaries containing the attributes and their values for each element. The function should only extract attributes from the opening tags of the HTML elements.
"""

import re

def parse_html_attributes(html: str) -> dict:
    tag_pattern = r'<(\w+)([^>]*)>'
    attribute_pattern = r'(\w+)="([^"]*)"'
    result = {}
    
    for match in re.finditer(tag_pattern, html):
        tag_name = match.group(1)
        attributes_str = match.group(2)
        attributes = dict(re.findall(attribute_pattern, attributes_str))
        result[tag_name] = attributes
    
    return result