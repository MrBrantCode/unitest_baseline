"""
QUESTION:
Create a function `format_url_as_hyperlink(input_string)` that takes a string as input, identifies the first URL in the string (either HTTP or HTTPS), and returns the URL as a clickable hyperlink in HTML format. If no URL is found, return the string "No URL found in the input string".
"""

import re

def format_url_as_hyperlink(input_string):
    # Regular expression to match URLs
    url_pattern = r'https?://\S+'

    # Find the URL in the input string
    url_match = re.search(url_pattern, input_string)

    if url_match:
        url = url_match.group(0)
        # Format the URL as a clickable hyperlink in HTML
        hyperlink = f'<a href="{url}">{url}</a>'
        return hyperlink
    else:
        return "No URL found in the input string"