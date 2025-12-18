"""
QUESTION:
Write a function called `extractBodyClasses` that takes a string representing well-formed HTML content as input and returns a list of unique class names found in the "body" tag. The input HTML content is guaranteed to contain a "body" tag, and the "body" tag may have multiple classes separated by spaces.
"""

import re

def extractBodyClasses(html_content):
    body_tag_pattern = re.compile(r'<body\s+class="([^"]*)"')
    match = body_tag_pattern.search(html_content)
    if match:
        classes = match.group(1).split()
        return list(set(classes))  # Return unique class names
    else:
        return []  # Return empty list if no class attribute found in body tag