"""
QUESTION:
Write a function `replace_url(match)` that replaces URLs with "URL" in a given text, excluding URLs that are within HTML anchor tags. The input text may contain multiple URLs and HTML anchor tags with URLs.
"""

import re

def replace_url(match):
    if match.group(1):  # If the match is an HTML anchor tag
        return match.group(1)
    else:
        return 'URL'