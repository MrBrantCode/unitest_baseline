"""
QUESTION:
Extract URLs from a list of strings using a function named `extract_urls`. The function should take a list of strings as input and return a list of extracted URLs. 

The URLs must meet the following criteria:
- Start with "http://" or "https://"
- Contain at least one dot (.) after the domain name
- Not contain any special characters or spaces, except for the following: dollar sign ($), hyphen (-), underscore (_), dot (.), tilde (~), forward slash (/), colon (:), question mark (?), number sign (#), at sign (@), exclamation mark (!), asterisk (*), plus sign (+), comma (,), semicolon (;), equals sign (=), apostrophe ('), percent sign (%), and ampersand (&).
"""

import re

def extract_urls(strings):
    urls = []
    pattern = r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
    
    for string in strings:
        matches = re.findall(pattern, string)
        for match in matches:
            if '.' in match and not re.search(r'[^a-zA-Z0-9\-._~:/?#@!$&\'()*+,;=%]', match):
                urls.append(match)
    
    return urls