"""
QUESTION:
Create a function named `extract_subdomain` that takes a URL string as input. The function should extract and return all subdomains from the URL, handling cases with multiple subdomains. If no subdomain is present, the function should return "No subdomain present". The function should be able to handle URLs of the format `https://subdomain1.subdomain2.example.com/path`. Note that validating the existence of a subdomain is not required.
"""

from urllib.parse import urlparse

def extract_subdomain(url):
    try:
        # parse the url to get the network location
        netloc = urlparse(url).netloc
        # split the network location to separate subdomains from main domain
        parts = netloc.split('.')
        # if there's only two parts, it means no subdomain is present
        if len(parts) < 3:
            return "No subdomain present"
        else:
            # join all parts except last two (main domain) to extract subdomain(s)
            return ".".join(parts[:-2])
    except Exception as e:
        return str(e)