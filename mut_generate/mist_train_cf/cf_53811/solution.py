"""
QUESTION:
Create a function named `process_url` that takes a URL string as input and returns a tuple containing the URL's smallest form and a dictionary representing its hierarchy. The smallest form should be the base URL (scheme + netloc), and the hierarchy should be a dictionary of URL components in descending order (fragment, query, path, netloc, scheme). The function should handle exceptions pertaining to invalid URL formatting, returning `None` for the smallest URL and an empty dictionary for hierarchy in such cases.
"""

from urllib.parse import urlsplit, urlunsplit

def process_url(url):
    try:
        url_obj = urlsplit(url)
        smallest_url = urlunsplit((url_obj.scheme, url_obj.netloc, '', '', ''))
        hierarchy = { 
            "scheme": url_obj.scheme, 
            "netloc": url_obj.netloc, 
            "path": url_obj.path, 
            "query": url_obj.query, 
            "fragment": url_obj.fragment 
        }
        hierarchy = {k: v for k, v in reversed(list(hierarchy.items()))}

    except ValueError as e:
        print(f'Invalid URL: {e}')
        smallest_url, hierarchy = None, {}

    return smallest_url, hierarchy