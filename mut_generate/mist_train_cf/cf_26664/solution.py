"""
QUESTION:
Create a function `extractAndCleanAnchorTags` that takes a string `html` as input. The input string contains HTML anchor tags and possibly zero-width non-joiner characters represented by "&zwnj;". Return a list of text content from the anchor tags with all "&zwnj;" removed. The function should not rely on any external libraries other than Python's standard library, and should handle multiple anchor tags in the input string.
"""

import re

def extractAndCleanAnchorTags(html):
    pattern = r'<a[^>]*>(.*?)</a>'
    matches = re.findall(pattern, html)
    cleaned_text = [match.replace('&zwnj;', '') for match in matches]
    return cleaned_text