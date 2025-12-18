"""
QUESTION:
Write a function `is_html_tag` that determines whether a given string is a well-formed HTML tag. The function should return `True` if the string is a well-formed HTML tag and `False` otherwise. A well-formed HTML tag is defined as a string that starts with '<', followed by one or more non-'/' and non-'>' characters, followed by zero or more non-'>' characters, followed by '>', then any characters, followed by '</', the same tag name as at the start of the string, and finally '>'. The function should not consider self-closing tags as well-formed.
"""

import re

def is_html_tag(test_string):
    pattern = r'<\s*([^\/>]+)([^>]*)>(.*?)<\/\s*([^\s>]+)\s*>'
    html_match = re.match(pattern, test_string)
    # check if match found and opening and closing tags are same
    if html_match and html_match.group(1) == html_match.group(4):
        return True
    else:
        return False