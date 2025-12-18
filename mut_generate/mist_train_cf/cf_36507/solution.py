"""
QUESTION:
Write a function `countUniqueCSSProperties(css)` that takes a string `css` representing the content of a CSS file and returns the count of unique CSS properties used within it. A CSS property is considered unique if it appears with a different value or in a different context within the file. The function should ignore any comments and only consider properties that are within the scope of a CSS rule.
"""

import re

def count_unique_css_properties(css):
    properties = set()
    css_rules = re.findall(r'(?<=\{)(.*?)(?=\})', css, re.DOTALL)
    for rule in css_rules:
        property_value_pairs = re.findall(r'(\w+-?\w*):[^;]+;', rule)
        for pair in property_value_pairs:
            properties.add(pair.strip())
    return len(properties)