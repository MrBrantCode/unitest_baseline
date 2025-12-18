"""
QUESTION:
Create a function called `validate_html_input` that validates whether a given HTML string has properly nested HTML tags and attributes. The function should return `True` if the HTML string is valid and `False` otherwise.
"""

import re

def validate_html_input(html_input):
    stack = []
    pattern = r"<\s*([a-zA-Z]+)(\s*[a-zA-Z]+\s*=\s*\"[^\"]*\")*\s*>|<\s*/\s*([a-zA-Z]+)\s*>"

    tags = re.findall(pattern, html_input)
    
    for tag in tags:
        if tag[0]:  # Opening tag
            stack.append(tag[0])
        else:  # Closing tag
            if not stack:
                return False
            if tag[2] != stack.pop():
                return False
    
    return len(stack) == 0