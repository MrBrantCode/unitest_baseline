"""
QUESTION:
Create a function named `extract_domain` that takes a URL as input and returns the domain name, excluding any subdomains or paths, query parameters, and fragments. If the domain starts with "www.", it should be removed.
"""

import urllib.parse

def extract_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain