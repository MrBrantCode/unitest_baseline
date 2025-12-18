"""
QUESTION:
Write a function `parse_annotations` that takes a string `code_snippet` as input, extracts descriptions and numerical identifiers enclosed in Elo annotations (e.g., `[Elo("description", identifier)]`), and returns a dictionary where the descriptions are the keys and the numerical identifiers are the values. The descriptions and identifiers are enclosed in double quotes and parentheses, respectively, and are separated by a comma within the Elo annotations.
"""

import re

def parse_annotations(code_snippet):
    annotations = {}
    pattern = r'\[Elo\("(.*?)"\s*,\s*(\d+)\)\]'
    matches = re.findall(pattern, code_snippet)
    for match in matches:
        description, identifier = match
        annotations[description] = int(identifier)
    return annotations