"""
QUESTION:
Create a function named `extract_view_urls` that takes a list of Django URL patterns as input and returns a dictionary where the keys are the view names and the values are the corresponding URLs. The input URL patterns are strings in the format `url(<pattern>, <view_function>, name="<view_name>")`, where `<pattern>` is the URL pattern, `<view_function>` is the corresponding view function, and `<view_name>` is the name assigned to the view. The output dictionary should have the view names as keys and the URL patterns as values.
"""

import re

def extract_view_urls(url_patterns: list) -> dict:
    view_urls = {}
    for pattern in url_patterns:
        match = re.match(r'url\(r"(.+)",\s*(\w+\.\w+),\s*name="(\w+)"\)', pattern)
        if match:
            url, view_function, view_name = match.groups()
            view_urls[view_name] = url
    return view_urls