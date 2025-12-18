"""
QUESTION:
Write a function `strip_html_tags` that takes a string of HTML code as input and returns the string with all HTML tags stripped, handling nested tags correctly. The function should use regular expressions and recursion to ensure all tags are removed.
"""

import re

def strip_html_tags(html):
    # Regular expression pattern to match HTML tags
    tag_pattern = r'<[^>]+>'

    # Remove all HTML tags from the input string
    plain_text = re.sub(tag_pattern, '', html)

    # Check if any nested tags still remain
    if re.search(tag_pattern, plain_text):
        # If nested tags are found, recursively strip the remaining tags
        return strip_html_tags(plain_text)
    
    return plain_text