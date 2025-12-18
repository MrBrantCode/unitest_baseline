"""
QUESTION:
Create a function named `parse_url` that takes one parameter, a URL string. The function should use the `urllib.parse` library to extract the protocol, domain, and path segments from the URL. It must handle errors where the URL lacks a protocol or has a malformed path, and it should support both HTTP and HTTPS protocols.
"""

from urllib.parse import urlparse

def parse_url(url):
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc, result.path]):
            return {
                'protocol': result.scheme,
                'domain': result.netloc,
                'path': result.path
            }
        else:
            raise Exception("Invalid URL. Either Protocol, Domain, or Path is missing.")
    except Exception as e:
        raise Exception("Error occurred: " + str(e))