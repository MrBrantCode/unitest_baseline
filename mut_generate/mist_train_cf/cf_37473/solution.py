"""
QUESTION:
Create a function named `match_url` that takes a URL string and returns the name of the corresponding view function based on predefined URL patterns. The function should iterate through the URL patterns, check for a match with the given URL, and return the corresponding view function name. If no match is found, return 'Not Found'. 

The predefined URL patterns are:
- `appleupdate`: `^appleupdate/(?P<serial>[^/]+)$`
- `raw`: `^raw/(?P<serial>[^/]+)$`
- `submit`: `^submit/(?P<submission_type>[^/]+)$` and `^(?P<submission_type>[^/]+)$`
- `warranty`: `^warranty/(?P<serial>[^/]+)$`
- `lookup_ip`: `^ip$`
"""

import re

def match_url(url: str) -> str:
    url_patterns = [
        (r'^appleupdate/(?P<serial>[^/]+)$', 'appleupdate'),
        (r'^raw/(?P<serial>[^/]+)$', 'raw'),
        (r'^submit/(?P<submission_type>[^/]+)$', 'submit'),
        (r'^warranty/(?P<serial>[^/]+)$', 'warranty'),
        (r'^ip$', 'lookup_ip'),
        (r'^(?P<submission_type>[^/]+)$', 'submit')
    ]

    for pattern, view_function in url_patterns:
        match = re.match(pattern, url)
        if match:
            return view_function
    return 'Not Found'