"""
QUESTION:
Write a Python function `find_urls(text)` to find all URLs present in the given text. The function should return a list of URLs found in the text. The URLs may start with either `http://` or `https://`.
"""

import re

def find_urls(text):
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    found_urls = re.findall(url_pattern, text)
    return found_urls