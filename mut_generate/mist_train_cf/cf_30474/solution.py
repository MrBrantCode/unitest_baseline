"""
QUESTION:
Create a function `extractLinks(html)` that takes a string `html` as input and returns a dictionary. The dictionary should contain the URLs from the `href` attributes of anchor tags in the HTML code as keys and the corresponding link texts enclosed within `<span>` tags with the class `link-text` as values.
"""

import re

def extractLinks(html):
    link_pattern = r'<a\s+href="([^"]+)"[^>]*>\s*<span class="link-text">([^<]+)</span>\s*</a>'
    matches = re.findall(link_pattern, html)
    return {url: text for url, text in matches}