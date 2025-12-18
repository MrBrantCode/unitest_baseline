"""
QUESTION:
Create a function `url_check(url_name)` that takes a string representing a URL and returns 'Valid' if the URL is valid and 'Invalid' otherwise. The URL is considered valid if it meets the following conditions: 
- It starts with 'http://' or 'https://'. 
- It contains only alphanumerics, dot ('.'), slash ('/'), hyphen ('-'), underscore ('_'), and at most three '#' hash symbols. 
- There are no more than two slashes ('/') in a row. 
- The URL does not end with a slash ('/'). 
- At least one dot ('.') appears after the 'http://' or 'https://'. 
- The substring before the first dot is not empty and contains only alphanumeric characters or hyphens. 
- The substring after the last dot is one of these: ['com', 'org', 'edu', 'gov', 'net', 'io']. 
- The length of the URL is between 10 and 100 characters.
"""

import re

def url_check(url_name):
    if 10 <= len(url_name) <= 100:
        protocol_pattern = re.compile(r'^https?://')
        protocol_match = protocol_pattern.match(url_name)
        if protocol_match:
            clean_url = protocol_pattern.sub("", url_name)
            if clean_url.count('/') <= 2 and clean_url.count('#') <= 3 and clean_url[-1] != '/' and '.' in clean_url:
                substrings = clean_url.split('.')
                if len(substrings[0]) > 0 and all(char.isalnum() or char=='-' for char in substrings[0]):
                    if substrings[-1] in ['com', 'org', 'edu', 'gov', 'net', 'io']:
                        if all(char.isalnum() or char in ['.','/','-','_','#'] for char in clean_url):
                            return 'Valid'
    return 'Invalid'