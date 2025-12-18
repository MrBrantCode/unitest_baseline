"""
QUESTION:
Create a function called `parse_url` that takes a URL string as input and returns a dictionary containing the URL's components. The function should be able to parse URLs in the following formats: 

- https://www.example.com/path/page.html
- http://example.com/page.html
- www.example.com
- example.com/page.html

The function should also be able to handle URLs with query parameters (e.g., https://www.example.com/path/page.html?param=value&param2=value2) and URLs with fragments (e.g., https://www.example.com/path/page.html#fragment). 

The returned dictionary should contain the following keys: "protocol", "domain", "path", "params", and "fragment". The "params" value should be another dictionary containing the query parameters as key-value pairs. 

Assume all URLs passed to the function are valid and well-formed according to the supported formats. Do not use any URL parsing libraries or functions; all parsing must be done with regex and string manipulation methods.
"""

import re

def parse_url(url_str):
    result = {}

    pattern = re.compile(r'^(?:(?P<protocol>https?):\/\/)?(?P<domain>(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,4}))?(?P<path>\/[^\?#]*)?(?:\?(?P<params>[^#]*))?(?:#(?P<fragment>.*))?$', re.IGNORECASE)                              
    m = pattern.match(url_str)

    if m:
        result["protocol"] = m.group("protocol") if m.group("protocol") else ""
        result["domain"] = m.group("domain") if m.group("domain") else ""
        result["path"] = m.group("path") if m.group("path") else ""
        result["fragment"] = m.group("fragment") if m.group("fragment") else ""
        result["params"] = {}

        param_str = m.group("params")
        if param_str:
            param_pairs = param_str.split("&")
            for pair in param_pairs:
                k, v = pair.split("=")
                result["params"][k] = v

    return result