"""
QUESTION:
Write a function `replace_url` that takes a string as input and returns the string with all URLs replaced by "URL", except for URLs that are within HTML anchor tags.
"""

import re

def replace_url(text):
    # Define the regular expression pattern
    pattern = r'(<a.*?>.*?</a>)|((?:http|https):\/\/[^\s]+)'

    # Function to handle the replacement
    def handle_match(match):
        if match.group(1):  # If the match is an HTML anchor tag
            return match.group(1)
        else:
            return 'URL'

    # Perform the replacement
    return re.sub(pattern, handle_match, text)