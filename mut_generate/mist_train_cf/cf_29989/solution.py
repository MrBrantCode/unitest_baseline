"""
QUESTION:
Implement a function `countHTMLTags` that takes a string `htmlSnippet` as input and returns the count of HTML tags present in the snippet. An HTML tag is defined as a string enclosed within angle brackets, and self-closing tags (e.g., `<br/>`) should not be counted as two separate tags.
"""

import re

def countHTMLTags(htmlSnippet):
    tag_pattern = r'<[^>]+>'
    tags = re.findall(tag_pattern, htmlSnippet)
    return len(tags)