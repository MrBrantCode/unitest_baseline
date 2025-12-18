"""
QUESTION:
Create a function `extract_URLs` that takes a string as an input, extracts and differentiates between HTTP and HTTPS URLs, and returns them as a tuple of two lists: the first list containing HTTP URLs and the second list containing HTTPS URLs. The function should ignore URLs with protocols other than HTTP and HTTPS, as well as non-URL texts.
"""

import re

def extract_URLs(string):
    http_pattern  = re.compile(r'(http://[^\s]+)')
    https_pattern = re.compile(r'(https://[^\s]+)')
    
    http_urls = re.findall(http_pattern, string)
    https_urls = re.findall(https_pattern, string)
    return (http_urls, https_urls)