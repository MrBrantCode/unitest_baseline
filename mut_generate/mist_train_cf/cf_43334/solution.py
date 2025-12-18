"""
QUESTION:
Write a function `extract_css_properties(html_code: str) -> List[str]` that takes an HTML code snippet as input and returns a list of CSS properties found within the style attribute of the HTML elements. The CSS properties should be returned in their original format, including the semicolon at the end. The function should be able to handle multiple style attributes and properties in the input HTML code.
"""

from typing import List
import re

def extract_css_properties(html_code: str) -> List[str]:
    css_properties = []
    pattern = r'style="([^"]*)"'
    matches = re.findall(pattern, html_code)
    for match in matches:
        properties = match.split(';')
        for prop in properties:
            if prop.strip():
                css_properties.append(prop.strip() + ';')
    return css_properties