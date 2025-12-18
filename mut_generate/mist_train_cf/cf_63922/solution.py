"""
QUESTION:
Write a function `parse_url(url)` that takes a URL as input and returns its components. The function should extract the protocol, domain, subdomain (if any), path, and query parameters (if any). It should handle cases where the URL might be missing certain components, has extra slashes, or is invalid. If the URL does not start with 'http://' or 'https://', it should be assumed to start with 'http://'. The function should return the extracted components, handling any exceptions that may occur.
"""

from urllib.parse import urlparse, parse_qs

def parse_url(url):
    """
    This function takes a URL as input, extracts its components, 
    and returns them. The function handles cases where the URL might 
    be missing certain components, has extra slashes, or is invalid.

    Args:
        url (str): The URL to be parsed.

    Returns:
        dict: A dictionary containing the protocol, domain, subdomain, 
        path, and query parameters of the URL.
    """

    try:
        # Add http prefix if not in url
        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        # Parsing the URL
        parsed_url = urlparse(url)

        # Extracting protocol
        protocol = parsed_url.scheme

        # Extracting domain and subdomain
        domain = ".".join(parsed_url.netloc.split(".")[-2:])

        subdomain_list = parsed_url.netloc.split(".")[:-2]
        subdomain = ".".join(subdomain_list) if len(subdomain_list) > 0 else None

        # Extracting path
        path = parsed_url.path

        # Extracting query parameters
        query_params = parse_qs(parsed_url.query)

        # Returning the components of URL
        return {
            "protocol": protocol,
            "domain": domain,
            "subdomain": subdomain,
            "path": path,
            "query_params": query_params
        }

    except Exception as e:
        print("Invalid URL, please try again!")
        print("Error: ", str(e))
        return None