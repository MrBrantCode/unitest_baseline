"""
QUESTION:
Write a Python function named `find_url` that takes a string as input and returns a list of all URLs found in the string. The function should be able to identify both HTTP and HTTPS URLs and should handle most common URL characters.
"""

import re

def find_url(string): 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url