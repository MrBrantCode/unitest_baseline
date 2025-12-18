"""
QUESTION:
Create a function `extractDivContent(html: str) -> str` that takes an HTML snippet as input and returns the text content within the `<div>` tags with class "section-title". The function should return "No <div> tag with class 'section-title' found in the HTML snippet." if no matching tag is found.
"""

import re

def extractDivContent(html: str) -> str:
    match = re.search(r'<div class="section-title[^>]*>(.*?)</div>', html)
    if match:
        return match.group(1)
    else:
        return "No <div> tag with class 'section-title' found in the HTML snippet."