"""
QUESTION:
Construct a function named `constructURL` that takes in the following parameters: `subdomain`, `domain`, `ccTLD`, `path`, `parameters`, and `fragment`. The function should construct a URL using these parameters and return the constructed URL. 

Construct another function named `validateURL` that takes a URL as input, validates it, and returns a boolean indicating whether the URL is valid along with an error message if the URL is invalid. The validation should check for the existence of a protocol, a valid domain or subdomain, and a resource path. The function should also support various protocols including sftp, http, and https.

The functions should handle and distinguish between POST and GET requests and should appropriately process Unicode characters in the URL, query parameters, and fragment identifiers. They should also include broad and specific error handling techniques for malformed URLs or their components. The functions should output specific error messages for invalid or missing protocol, domain, subdomain, resource path, query parameters, and fragment identifiers.

Additionally, implement functions to ensure valid URL encoding, parse URLs into components, and manage errors. The functions should be able to keep a record of all errors encountered while trying to access the URL and provide the number of occurrences of each individual error, along with potential solutions to each type of error encountered.
"""

import urllib.parse

def constructURL(subdomain, domain, ccTLD, path, parameters={}, fragment=None):
    """
    Construct a URL using the given parameters.

    Args:
        subdomain (str): The subdomain of the URL.
        domain (str): The domain of the URL.
        ccTLD (str): The country-code top-level domain of the URL.
        path (str): The path of the URL.
        parameters (dict): The query parameters of the URL. Defaults to {}.
        fragment (str): The fragment of the URL. Defaults to None.

    Returns:
        str: The constructed URL.
    """
    netloc = subdomain + "." + domain + ccTLD
    url = urllib.parse.urlunparse(('http', netloc, path, None, urllib.parse.urlencode(parameters), fragment))

    return url

def validateURL(url):
    """
    Validate a URL.

    Args:
        url (str): The URL to validate.

    Returns:
        tuple: A tuple containing a boolean indicating whether the URL is valid and an error message if it's not.
    """
    parsed = urllib.parse.urlparse(url)
    
    if len(parsed.scheme) == 0:
        return False, "Missing protocol"
    if len(parsed.netloc.split(".")) < 2:
        return False, "Invalid domain or subdomain"
    if parsed.path == '':
        return False, "Missing resource path"
    
    return True, None