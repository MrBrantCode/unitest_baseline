"""
QUESTION:
Write a function `convert_tags_to_lowercase` that transforms the given HTML string by converting all HTML tags to lowercase while preserving the case sensitivity of attribute values and texts enclosed between start and end tags. The function should not modify the original string and return the transformed string.
"""

import re

def convert_tags_to_lowercase(html_string):
    """
    This function transforms the given HTML string by converting all HTML tags to lowercase 
    while preserving the case sensitivity of attribute values and texts enclosed between 
    start and end tags.

    Args:
        html_string (str): The input HTML string.

    Returns:
        str: The transformed HTML string with all tags in lowercase.
    """

    # Regular expression that matches the tags
    tag_pattern = re.compile(r'(<[/!]?)(.*?)(>)')

    # Function to convert HTML tags to lowercase
    def convert_match(match):
        return f'{match.group(1)}{match.group(2).lower()}{match.group(3)}'

    # Convert HTML tags to lowercase
    return tag_pattern.sub(convert_match, html_string)