"""
QUESTION:
Create a function `find_url` that takes a string as input and returns a list of HTTP and HTTPS URLs found in the string. The function should exclude URLs that contain any of the given forbidden words or patterns. The regex pattern should allow alphanumeric characters and special characters. The function should be case sensitive and the forbidden words should be matched as whole words only.
"""

import re

def find_url(string, forbidden):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(string)

    return [url for url in urls if not any(word in url for word in forbidden)]