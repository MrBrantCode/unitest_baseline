"""
QUESTION:
Create a function `extractBackgroundImageURL(html: str, password: str) -> str` that takes in an HTML code snippet as a string and a password as a string, and returns the final URL of the background image after replacing the `<PASSWORD>` placeholder in the URL embedded within the `style` attribute of a `div` element. Assume the HTML code snippet will always contain a single `div` element with a `style` attribute containing the background image URL, and the `<PASSWORD>` placeholder will always be present in the URL.
"""

import re

def extractBackgroundImageURL(html: str, password: str) -> str:
    # Use regular expression to extract the URL from the style attribute
    url_match = re.search(r"background-image: url\('([^']+)<PASSWORD>([^']+)'\)", html)
    
    if url_match:
        # Replace the <PASSWORD> placeholder with the actual password
        final_url = url_match.group(1) + password + url_match.group(2)
        return final_url
    else:
        return "URL not found or invalid HTML format"