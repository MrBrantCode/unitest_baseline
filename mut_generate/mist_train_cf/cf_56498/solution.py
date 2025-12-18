"""
QUESTION:
Create a function called `find_urls` that takes a string as input and returns a list of all URLs (both HTTP and HTTPS) found in the string. The function should be able to handle URLs with diverse structural composition and length. The URLs must start with either "http://" or "https://". The function should use regular expressions to match the URLs.
"""

import re

def find_urls(string):
    pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    return re.findall(pattern, string)