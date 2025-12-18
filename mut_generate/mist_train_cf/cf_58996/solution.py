"""
QUESTION:
Write a function named `extract_domain_name` that takes a URL as input and returns the name of the website, excluding any subdomains (like 'www') and top-level domains (like '.com', '.org', '.io', '.gov', '.net', etc.).
"""

from urllib.parse import urlparse

def extract_domain_name(url):
    domain = urlparse(url).netloc.split('.')
    if 'www' in domain[0]:
        return domain[1]
    else:
        if len(domain) > 2:
            return domain[-2]
        else:
            return domain[0]