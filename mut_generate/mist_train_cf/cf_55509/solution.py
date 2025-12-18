"""
QUESTION:
Create a function `extract_textual_content(html_string)` that uses regular expressions to extract the textual content between HTML tags, including nested tags and self-closing tags, in a given HTML string. The function should return a list of extracted textual content without the HTML tags.
"""

import re

def extract_textual_content(html_string):
    """
    This function uses regular expressions to extract the textual content 
    between HTML tags, including nested tags and self-closing tags, 
    in a given HTML string.
    
    Args:
        html_string (str): The input HTML string.
    
    Returns:
        list: A list of extracted textual content without the HTML tags.
    """
    pattern = re.compile(r'<[^>]*>([^<]*)</[^>]*>')
    matches = pattern.findall(html_string)
    return [match.strip() for match in matches]