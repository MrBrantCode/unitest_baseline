"""
QUESTION:
Create a function called `organize_urls` that takes a list of URLs as input and returns a dictionary where the keys are the domain names (excluding the protocol) and the values are lists of unique URLs associated with each domain. The function should handle duplicate URLs and ensure that each URL is only listed once per domain.
"""

from urllib.parse import urlparse

def organize_urls(urls):
    domain_urls = {}
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain not in domain_urls:
            domain_urls[domain] = [url]
        else:
            if url not in domain_urls[domain]:
                domain_urls[domain].append(url)
    return domain_urls