"""
QUESTION:
Extract the attributes (id, class, name, type, and value) from a given HTML button element string and return them in a dictionary. The input string is well-formed and contains at least one of the specified attributes. The function should be implemented with the following signature: `def extract_button_attributes(html_button: str) -> dict`.
"""

import re

def extract_button_attributes(html_button: str) -> dict:
    attributes = {}
    matches = re.search(r'<button\s+([^>]*)>([^<]*)</button>', html_button)
    if matches:
        attr_str = matches.group(1)
        attr_pairs = re.findall(r'(\w+)="([^"]+)"', attr_str)
        for key, value in attr_pairs:
            attributes[key] = value
    return attributes