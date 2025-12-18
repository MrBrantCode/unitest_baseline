"""
QUESTION:
Write a function called `extract_domain` that takes a URL string as input and returns the domain name excluding any subdomains. The domain name should be in the format of "example.com" where "example" is the domain and "com" is the top-level domain. The function should handle URLs with both HTTP and HTTPS protocols.
"""

from urllib.parse import urlparse
def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]
    return domain