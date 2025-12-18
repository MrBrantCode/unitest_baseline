"""
QUESTION:
Implement the `extract_html_attributes` function to extract all attributes from the opening tags in a given HTML string. The function takes a string containing HTML code as input and returns a list of all the attributes found, where each attribute is represented as a single string in the format 'attribute="value"'. Ensure the function handles various HTML tag structures and attribute formats, including single and double quotes, spaces, and different attribute orders.
"""

import re

def extract_html_attributes(html_string):
    pattern = r'<\w+\s+([^>]+)>'
    matches = re.findall(pattern, html_string)
    attributes = []
    for match in matches:
        attr_pattern = r'(\w+)=["\']([^"\']*)["\']'
        attrs = re.findall(attr_pattern, match)
        for attr in attrs:
            attributes.append(f'{attr[0]}="{attr[1]}"')
    return attributes