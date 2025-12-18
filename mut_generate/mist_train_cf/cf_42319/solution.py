"""
QUESTION:
Write a function `analyzeHtmlCode` that takes a string of HTML code as input and returns a dictionary containing the count of each HTML element and attribute present in the code, ignoring case sensitivity. The dictionary should have the HTML elements and attributes as keys, and their respective counts as values.
"""

import re

def analyzeHtmlCode(html_code):
    element_pattern = r'<(\w+)[^>]*>'
    attribute_pattern = r'(\w+)="([^"]*)"'

    elements = re.findall(element_pattern, html_code, re.IGNORECASE)
    attributes = re.findall(attribute_pattern, html_code, re.IGNORECASE)

    element_counts = {}
    attribute_counts = {}

    for element in elements:
        element = element.lower()
        element_counts[element] = element_counts.get(element, 0) + 1

    for attribute in attributes:
        attribute_name = attribute[0].lower()
        attribute_counts[attribute_name] = attribute_counts.get(attribute_name, 0) + 1

    result = {**element_counts, **attribute_counts}
    return result