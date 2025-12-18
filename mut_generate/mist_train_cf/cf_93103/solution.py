"""
QUESTION:
Create a function `remove_html_tags` that takes an input string, removes all HTML tags and their content, and converts HTML entities to their corresponding characters. The function should not modify any characters that are not part of an HTML tag or entity.
"""

import re
import html

def remove_html_tags(input_string):
    # Remove HTML tags and content inside them
    clean_string = re.sub('<[^<]+?>', '', input_string)
    
    # Convert HTML entities to characters
    clean_string = html.unescape(clean_string)
    
    return clean_string