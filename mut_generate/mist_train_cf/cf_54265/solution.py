"""
QUESTION:
Create a function `find_urls` that takes an input string and returns a list of URLs found in the string. The function should identify any type of Uniform Resource Locator (URL) embedded within the input string. The identified URLs should start with either 'http://' or 'https://'.
"""

import re

def find_urls(input_text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls_found = re.findall(url_pattern, input_text)
    return urls_found