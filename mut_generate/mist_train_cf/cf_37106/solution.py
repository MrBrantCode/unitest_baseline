"""
QUESTION:
Create a function `extractUniqueColors(css)` that takes a string `css` containing CSS class definitions and returns a sorted list of unique color values used in those classes. Each class definition is in the format ".class-name {color: value;}" where the color value can be specified in various formats such as hexadecimal, RGB, or color names. Assume the input CSS string is well-formed and contains at least one class definition, and the color values are valid.
"""

from typing import List
import re

def extractUniqueColors(css: str) -> List[str]:
    color_values = set()
    pattern = r'color:\s*([^;}]+)'
    matches = re.findall(pattern, css)
    for match in matches:
        color_values.add(match.strip())
    return sorted(list(color_values))