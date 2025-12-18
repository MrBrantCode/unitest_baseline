"""
QUESTION:
Write a function named `extract_urls` that takes a string `input_text` as input and returns a list of all URLs (including http, https, and ftp links) found in the string. The function should be able to differentiate and isolate URLs from other alphanumeric character sequences in the input string.
"""

import re

def extract_urls(input_text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|ftp://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, input_text)
    return urls