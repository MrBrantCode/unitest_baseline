"""
QUESTION:
Write a function named `validate_html_input` that validates the nesting of HTML tags in a given input string. The function should return `True` if the tags are properly nested and closed, and `False` otherwise. The input string can contain HTML tags with or without attributes.
"""

import re

def validate_html_input(html_input):
    """
    Validate the nesting of HTML tags in a given input string.

    Args:
        html_input (str): The input string containing HTML tags.

    Returns:
        bool: True if the tags are properly nested and closed, False otherwise.
    """
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