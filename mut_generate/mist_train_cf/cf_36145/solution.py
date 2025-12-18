"""
QUESTION:
Implement a function `extract_div_attributes` that takes a string `html_snippet` representing an HTML snippet as input and returns a list of dictionaries, where each dictionary represents the attributes of a single `<div>` tag in the snippet. The function should be able to handle multiple `<div>` tags with varying attributes. 

The function should return a list of dictionaries where each dictionary key is the attribute name and the corresponding value is the attribute value. The function should only consider attributes that have a value enclosed in double quotes or single quotes.
"""

from typing import List, Dict
import re

def extract_div_attributes(html_snippet: str) -> List[Dict[str, str]]:
    div_attributes = []
    div_pattern = re.compile(r'<div\s+([^>]+)>')
    attribute_pattern = re.compile(r'(\w+)\s*=\s*["\']([^"\']+)["\']')

    div_matches = div_pattern.findall(html_snippet)
    for match in div_matches:
        attributes = {}
        attribute_matches = attribute_pattern.findall(match)
        for attr, value in attribute_matches:
            attributes[attr] = value
        div_attributes.append(attributes)

    return div_attributes