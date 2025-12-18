"""
QUESTION:
Create a function `count_domain_occurrences` that takes a list of URLs as input and returns a dictionary containing the domain names as keys and the number of occurrences as values. The function should handle URLs with different protocols, with and without "www" subdomain, and with different paths and query parameters. It should also handle invalid URLs that may raise exceptions. The function should ignore the "www." subdomain when counting occurrences.
"""

from typing import List, Dict
from urllib.parse import urlparse

def count_domain_occurrences(urls: List[str]) -> Dict[str, int]:
    domain_counts = {}
    for url in urls:
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.lower()
            if domain.startswith("www."):
                domain = domain[4:]
            if domain in domain_counts:
                domain_counts[domain] += 1
            else:
                domain_counts[domain] = 1
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
    return domain_counts