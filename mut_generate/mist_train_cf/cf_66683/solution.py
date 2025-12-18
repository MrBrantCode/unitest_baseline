"""
QUESTION:
Create a function called `extract_url` that takes a string of text as input and returns a list of all URLs found in the text. The function should be able to match both HTTP and HTTPS URLs. The regular expression used should be precise enough to differentiate between URLs and similar patterns, but it is acceptable if it is not perfect and may capture some non-URL strings or miss some URLs.
"""

import re

def extract_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    return urls