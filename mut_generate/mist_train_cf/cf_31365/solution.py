"""
QUESTION:
Implement a function `extractURLs` that takes an HTML snippet as input and returns a list of URLs extracted from the `href` attributes of the `NavLink` elements. The function should be able to handle multiple `NavLink` elements within the HTML snippet. The input HTML snippet will be provided as a string and the function should return a list of extracted URLs as strings.
"""

import re

def extractURLs(html_snippet):
    pattern = r'<NavLink\s+href="([^"]+)"'
    urls = re.findall(pattern, html_snippet)
    return urls