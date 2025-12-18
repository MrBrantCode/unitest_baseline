"""
QUESTION:
Write a function named `remove_html_tags` that takes a string input and returns the input string with all HTML tags and content inside them removed, and all HTML entities converted to their corresponding characters.
"""

import re
import html

def remove_html_tags(input_string):
    # Remove HTML tags and content inside them
    clean_string = re.sub('<[^<]+?>', '', input_string)
    
    # Convert HTML entities to characters
    clean_string = html.unescape(clean_string)
    
    return clean_string