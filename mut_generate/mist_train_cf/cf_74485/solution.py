"""
QUESTION:
Construct a function `construct_url` that creates a complete HTTP request URL given the protocol, subdomain, primary domain, resource path, and query parameters. The function should also verify if the constructed URL is valid. 

The function should accept the following parameters: 
- protocol (string): The protocol of the URL (e.g., "https")
- subdomain (string): The subdomain of the URL (e.g., "mypage")
- primary_domain (string): The primary domain of the URL (e.g., "google")
- resource_path (string): The resource path of the URL (e.g., "/search")
- params (dictionary): A dictionary of query parameters (e.g., {'q': 'python', 'oq': 'python'})

The function should return the constructed URL if it is valid, or an error message if it is not. The query parameters should be URL-encoded.
"""

from urllib.parse import urlparse, urlencode, urlunparse

def construct_url(protocol, subdomain, primary_domain, resource_path, params):
    netloc = subdomain + '.' + primary_domain + '.com'
    url_tuple = (protocol, netloc, resource_path, "", urlencode(params, doseq=True), "")
    url = urlunparse(url_tuple)
    
    if all([urlparse(url).scheme, urlparse(url).netloc]):
        return url
    else:
        return "Invalid URL components!"