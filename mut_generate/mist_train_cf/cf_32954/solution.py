"""
QUESTION:
Write a function named `extract_urls_from_html_comment` that takes a string representing an HTML comment containing anchor tags as input, extracts the URLs from the `href` attributes of the anchor tags within the HTML comment, and returns a list of the extracted URLs in the order they appear. The input string is guaranteed to be a valid HTML comment and the anchor tags have a single `href` attribute specifying the URL.
"""

import re

def extract_urls_from_html_comment(html_comment):
    anchor_tags = re.findall(r'<a\s+href="([^"]+)"', html_comment)
    return anchor_tags