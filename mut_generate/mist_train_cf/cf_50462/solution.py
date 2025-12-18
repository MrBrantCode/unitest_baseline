"""
QUESTION:
Write a function named `extract_ftp_urls` that takes a Unicode character string `s` as input and returns a list of all FTP URLs found in the string. The function should use regular expressions to match the FTP URLs, which start with "ftp://" followed by one or more alphanumeric characters, dots, slashes, colons, or hyphens.
"""

import re

def extract_ftp_urls(s):
    pattern = r'ftp://[a-zA-Z0-9\.:/-]+'
    ftp_urls = re.findall(pattern, s)    
    return ftp_urls