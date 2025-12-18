"""
QUESTION:
Create a function `extract_text_from_html(html)` that takes a string `html` representing one or more HTML elements and returns a list of the text content within the tags. The HTML elements will be in the format `<tag>text content</tag>`. The function should handle multiple HTML elements within the input string.
"""

import re

def extract_text_from_html(html):
    pattern = r'<[^>]*>'
    clean_html = re.sub(pattern, '', html)  # Remove all HTML tags
    return [clean_html.strip()]  # Return the extracted text content as a list