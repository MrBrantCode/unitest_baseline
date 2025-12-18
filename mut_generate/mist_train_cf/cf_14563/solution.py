"""
QUESTION:
Write a function named `parse_domain_name` that takes a URL as input and returns the domain name. The function should handle different protocols (HTTP, HTTPS), subdomains, query parameters, port numbers, and invalid characters in the domain name. If the URL starts with "www", it should be removed. If the URL contains a port number, it should be removed. If the URL contains any invalid characters in the domain name (e.g., special characters), the function should return "Invalid URL". The function should be able to handle URLs with different scenarios, such as "https://example.com/page?param1=value1&param2=value2" and "https://www.example.com:8080/page".
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