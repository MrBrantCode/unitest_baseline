"""
QUESTION:
Write a function called `count_unique_url_requests` that takes a list of URL requests as input. The function should count the number of unique requests, ignoring requests with the same URL but different query parameters, and return a dictionary with the total number of requests for each unique URL sorted in descending order based on their request count. The function should only use a single loop to process the URL requests.
"""

from collections import defaultdict
from urllib.parse import urlparse

def count_unique_url_requests(url_requests):
    url_counts = defaultdict(int)
    
    for url_request in url_requests:
        # Split the URL into base and query
        base_url = urlparse(url_request).path
        
        # Increment the request count for the base URL
        url_counts[base_url] += 1

    # Sort the URLs based on their request count in descending order
    sorted_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)
    
    return dict(sorted_urls)