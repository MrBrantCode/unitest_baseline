"""
QUESTION:
Create a function named `extract_domain_names` that takes a list of URLs as input and returns a list of unique domain names extracted from the URLs. The function should handle various URL formats, including those with subdomains and different top-level domains. The output list should only contain unique domain names.
"""

from urllib.parse import urlparse

def extract_domain_names(urls):
    unique_domains = set()
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith("www."):
            domain = domain[4:]  # Remove "www." prefix
        unique_domains.add(domain)
    return list(unique_domains)