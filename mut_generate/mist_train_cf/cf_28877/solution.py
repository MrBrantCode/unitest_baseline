"""
QUESTION:
Create a function named `extract_stylesheet_links` that takes a string of HTML content as input. The function should extract all the stylesheet links present in the HTML content, where each stylesheet link is defined within a `<link>` tag with a `rel` attribute set to "stylesheet" and a `href` attribute pointing to the stylesheet file. The function should return a list of all the stylesheet links present in the HTML.
"""

import re

def extract_stylesheet_links(html_content):
    pattern = r'<link\s+rel="stylesheet"\s+href="([^"]+)"\s*/?>'
    stylesheet_links = re.findall(pattern, html_content)
    return stylesheet_links