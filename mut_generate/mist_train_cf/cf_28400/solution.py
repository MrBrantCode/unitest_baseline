"""
QUESTION:
Create a function `count_domain_occurrences` that takes a list of URLs as input and returns a dictionary containing unique domain names as keys and their occurrence counts as values. The function should ignore any subdomains or paths when counting occurrences.
"""

from urllib.parse import urlparse

def count_domain_occurrences(urls):
    domain_counts = {}
    for url in urls:
        domain = urlparse(url).netloc
        if domain in domain_counts:
            domain_counts[domain] += 1
        else:
            domain_counts[domain] = 1
    return domain_counts