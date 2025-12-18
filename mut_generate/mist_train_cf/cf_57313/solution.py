"""
QUESTION:
Write a function `extract_web_addresses` that takes a string as input and returns a list of HTTP and HTTPS web addresses found in the string. The function should use regular expressions to match the web addresses. Assume that the URLs are well-formed according to standard URL syntax.
"""

import re

def extract_web_addresses(text):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)