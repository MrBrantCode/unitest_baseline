"""
QUESTION:
Write a function `get_domain_name(url)` that takes a URL as input, parses it, and returns the domain name. The function should handle various scenarios including different protocols (e.g. FTP, SMTP), subdomains, query parameters, port numbers, and fragment identifiers. It should also handle cases where the URL contains a username and password, and where the URL contains invalid characters. If the URL contains multiple query parameters with the same key, the function should return the value of the last occurrence. If the domain name contains any invalid characters, the function should return 'Invalid URL'.
"""

import re
from urllib.parse import urlparse, parse_qs

def get_domain_name(url):
    # Remove the protocol if present
    url = re.sub(r'^\w+://', '', url)
    
    # Remove the fragment identifier if present
    url = url.split('#')[0]
    
    # Parse the URL to get the domain name
    parsed_url = urlparse('//' + url) # add '//' to ensure urlparse works correctly
    domain_name = parsed_url.netloc
    
    # Remove the subdomain if present
    domain_parts = domain_name.split('.')
    if len(domain_parts) > 2:
        domain_name = '.'.join(domain_parts[-2:])
    
    # Remove the port number if present
    domain_name = re.sub(r':\d+', '', domain_name)
    
    # Remove any invalid characters from the domain name
    if not re.match(r'^[a-zA-Z0-9.-]+$', domain_name):
        return 'Invalid URL'
    
    # Handle the case where the URL contains a username and password
    if parsed_url.username and parsed_url.password:
        domain_name = re.sub(r'^%s:%s@' % (parsed_url.username, parsed_url.password), '', domain_name)
    
    return domain_name