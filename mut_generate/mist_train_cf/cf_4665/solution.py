"""
QUESTION:
Create a function `extract_url_parts(url)` that takes a URL string as input, extracts its domain name, port number, path, query parameters, and fragment using a Regular Expression, and returns these extracted parts as a tuple of strings. Ensure the function handles edge cases such as URLs with special characters or non-standard port numbers, and is optimized for performance to handle large datasets efficiently.
"""

import re

def extract_url_parts(url):
    pattern = r'^((?:(?:https?|ftp):\/\/)?(?:[^:\n\r]+:[^@\n\r]+@)?(?:www\.)?((?:[^:/\n\r]+\.)*[^:/\n\r]+))?(?::(\d+))?([^?\n\r]*)?(?:\?([^#\n\r]*))?(?:#(.*))?$'
    match = re.match(pattern, url)
    
    if match:
        domain = match.group(1) if match.group(1) else ''
        port = match.group(3) if match.group(3) else ''
        path = match.group(4) if match.group(4) else ''
        query = match.group(5) if match.group(5) else ''
        fragment = match.group(6) if match.group(6) else ''
        return domain, port, path, query, fragment
    
    return None