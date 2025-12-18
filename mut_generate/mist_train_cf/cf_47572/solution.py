"""
QUESTION:
Create a function called `detect_domain` that takes a URL as input and returns the domain name along with its level (top-level, second-level, or lower-level) based on the number of parts in the domain name. The function should use the `urlparse` function from the `urllib.parse` module to parse the URL and extract the domain name. The domain level should be determined by the number of parts in the domain name (split by '.'), with 2 parts indicating a top-level domain, 3 parts indicating a second-level domain, and more than 3 parts indicating a lower-level domain.
"""

from urllib.parse import urlparse

def detect_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri) 
    domain_parts = domain.split('.')
    if len(domain_parts) == 2:
        return 'Top-level domain.', domain
    elif len(domain_parts) == 3:
        return 'Second-level domain.', domain
    elif len(domain_parts) > 3:
        return 'Lower-level domain.', domain
    else:
        return 'Invalid domain.', domain