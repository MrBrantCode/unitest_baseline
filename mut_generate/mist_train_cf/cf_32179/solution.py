"""
QUESTION:
Write a function `extractClassAttribute` that takes a string representing an HTML tag as input and returns the value of the class attribute if it exists, or an empty string if the class attribute is not present. The function should extract the class value from the input string, including any spaces if the class attribute contains multiple values.
"""

import re

def extractClassAttribute(tag: str) -> str:
    match = re.search(r'class="([^"]+)"', tag)
    if match:
        return match.group(1)
    else:
        return ""