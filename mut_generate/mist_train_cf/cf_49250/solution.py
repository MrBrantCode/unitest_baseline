"""
QUESTION:
Develop a function named `find_urls` that takes a string `text` as input and returns a list of all URLs present in the string. The function should be able to identify URLs that start with "http://" or "https://", followed by any valid URL characters. The function should use regular expressions to achieve this.
"""

import re

def find_urls(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    return urls