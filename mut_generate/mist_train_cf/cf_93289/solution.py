"""
QUESTION:
Write a function `parse_domain_name(url)` that takes a URL as input and returns the domain name. The function should handle the following cases:
- Remove the "www" from the start of the URL if present.
- Remove the port number if present.
- Return the domain name without any query parameters.
- Check for invalid characters in the domain name (e.g. special characters) and return "Invalid URL" if found.

The domain name can contain alphanumeric characters, hyphens, and periods.
"""

import re

def parse_domain_name(url):
    # Remove "www" from the start of the URL if present
    if url.startswith("www."):
        url = url[4:]
    
    # Remove port number if present
    url = re.sub(r':\d+', '', url)
    
    # Extract domain name
    match = re.search(r'([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', url)
    
    if match:
        domain_name = match.group(1)
        
        # Check for invalid characters
        if re.search(r'[^a-zA-Z0-9.-]', domain_name):
            return "Invalid URL"
        
        return domain_name
    else:
        return "Invalid URL"