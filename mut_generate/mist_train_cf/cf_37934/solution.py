"""
QUESTION:
Write a function `parseHTML` that takes a string representing a well-formed HTML snippet as input, where the snippet only contains non-nested opening tags with optional attributes. The function should return a dictionary where the keys are the tag names and the values are lists of attribute-value pairs for each tag. Assume that the HTML snippet does not contain any closing tags.
"""

import re

def parseHTML(html_snippet):
    tag_pattern = r'<(\w+)(?:\s+([^>]+))?>'
    tags = re.findall(tag_pattern, html_snippet)
    tag_dict = {}
    for tag, attributes in tags:
        attribute_pairs = re.findall(r'(\w+)="([^"]+)"', attributes or '')
        tag_dict[tag] = attribute_pairs
    return tag_dict