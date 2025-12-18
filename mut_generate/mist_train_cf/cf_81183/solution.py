"""
QUESTION:
Create a function named `validate_url` that takes one string argument representing a URL. This function should return `True` if the URL is valid and `False` otherwise. The URL can be in one of the following formats: 

- `https://www.example.com/path/page.html`
- `http://example.com`
- `www.example.com/page1/page2`
- `example.com/page_name.html`

The function should consider variations such as the presence or absence of 'www', 'https' or 'http', '.html' or other extensions, and multiple path layers. The function should also be flexible enough to cover different domain names and extensions (e.g., .com, .net, .org, etc.).
"""

import re

def validate_url(url):
    pattern = re.compile(r'^(https?:\/\/)?(www\.)?([a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?)$')
    if re.match(pattern, url):
        return True
    else:
        return False