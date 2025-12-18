"""
QUESTION:
Write a Python function called `url_details` that takes a URL string as input. The function should extract and print the protocol, domain name, and path of the URL. Additionally, it should extract all parameters from the query string, if any are found, and count the frequency of each letter in the domain name. The function should validate the URL based on RFC 3986 URI syntax components before extracting its details. If the URL is invalid, it should print "Invalid URL".
"""

import re
from urllib.parse import urlparse, parse_qs

def url_details(url):
    """
    Function to extract and print the URL details

    Args:
    url (str): the URL to be analyzed
    """

    # Validate URL based on RFC 3986
    regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ip
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, url) is None:
        print("Invalid URL")
        return

    # Parse the URL into six components
    parsed_url = urlparse(url)

    # Extract URL details
    protocol = parsed_url.scheme   # Get the protocol
    domain = parsed_url.netloc     # Get the domain name
    path = parsed_url.path         # Get the path
    
    print("Protocol: ", protocol)
    print("Domain: ", domain)
    print("Path: ", path)

    # Extract query parameters
    params = parse_qs(parsed_url.query)

    print("Parameters: ")
    for key, value in params.items():
        print(key, ": ", value)

    # Count the frequency of each letter in the domain name
    letters_frequency = {}
    for letter in domain:
        if letter.isalpha():
            letters_frequency[letter] = letters_frequency.get(letter, 0) + 1
            
    print("\nFrequency of each letter in Domain: ")
    for key, value in letters_frequency.items():
        print(key, ": ", value)