"""
QUESTION:
Extract the unique domain names from a list of seed URLs that are not present in a given list of known domain names.

Implement a Python function `extract_domains(headers, seeds, domains)` where `headers` is a dictionary containing HTTP headers, `seeds` is a list of initial URLs, and `domains` is a list of known domain names. The function should return a list of unique domain names extracted from the seed URLs, excluding any domain names already present in the `domains` list. 

Note: The `headers` parameter is not used in the function implementation, it is assumed to be a requirement for future extensions or other parts of the program.
"""

from urllib.parse import urlparse

def extract_domains(headers, seeds, domains):
    unique_domains = set(domains)  # Initialize with known domains to avoid duplicates
    for seed in seeds:
        parsed_url = urlparse(seed)
        domain = parsed_url.netloc
        if domain not in unique_domains:
            unique_domains.add(domain)

    return list(unique_domains)