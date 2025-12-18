"""
QUESTION:
Write a function `find_urls_in_text(text)` that takes a string `text` as input and returns a list of all URLs embedded within the text. The function should accurately identify both HTTP and HTTPS URLs, as well as URLs with query parameters and fragments. The function should use regular expressions to match the URLs.
"""

import re

def find_urls_in_text(text):
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    return urls